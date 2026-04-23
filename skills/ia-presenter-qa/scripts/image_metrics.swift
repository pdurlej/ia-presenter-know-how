#!/usr/bin/env swift

import AppKit
import CoreImage
import CoreImage.CIFilterBuiltins
import Foundation
import ImageIO
import Vision

struct Metrics: Codable {
    let path: String
    let width: Int
    let height: Int
    let averageLuminance: Double?
    let textObservationCount: Int
    let wordCount: Int
    let recognizedLines: [String]
    let textBoxAreaRatio: Double
    let leftTextAreaRatio: Double
    let rightTextAreaRatio: Double
    let topTextAreaRatio: Double
    let bottomTextAreaRatio: Double
    let largestBoxAreaRatio: Double
    let centerTextX: Double?
    let centerTextY: Double?
}

let context = CIContext(options: [.workingColorSpace: NSNull(), .outputColorSpace: NSNull()])

func loadCGImage(from url: URL) -> CGImage? {
    guard let source = CGImageSourceCreateWithURL(url as CFURL, nil) else { return nil }
    return CGImageSourceCreateImageAtIndex(source, 0, nil)
}

func averageLuminance(for image: CGImage) -> Double? {
    let ciImage = CIImage(cgImage: image)
    let filter = CIFilter.areaAverage()
    filter.inputImage = ciImage
    filter.extent = ciImage.extent
    guard let output = filter.outputImage else { return nil }
    var bitmap = [UInt8](repeating: 0, count: 4)
    context.render(
        output,
        toBitmap: &bitmap,
        rowBytes: 4,
        bounds: CGRect(x: 0, y: 0, width: 1, height: 1),
        format: .RGBA8,
        colorSpace: nil
    )
    let red = Double(bitmap[0]) / 255.0
    let green = Double(bitmap[1]) / 255.0
    let blue = Double(bitmap[2]) / 255.0
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue
}

func detectText(in url: URL) -> [VNRecognizedTextObservation] {
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .fast
    request.usesLanguageCorrection = false
    let handler = VNImageRequestHandler(url: url, options: [:])
    do {
        try handler.perform([request])
        return request.results ?? []
    } catch {
        return []
    }
}

func collectMetrics(for path: String) -> Metrics {
    let url = URL(fileURLWithPath: path)
    guard let image = loadCGImage(from: url) else {
        return Metrics(
            path: path,
            width: 0,
            height: 0,
            averageLuminance: nil,
            textObservationCount: 0,
            wordCount: 0,
            recognizedLines: [],
            textBoxAreaRatio: 0,
            leftTextAreaRatio: 0,
            rightTextAreaRatio: 0,
            topTextAreaRatio: 0,
            bottomTextAreaRatio: 0,
            largestBoxAreaRatio: 0,
            centerTextX: nil,
            centerTextY: nil
        )
    }

    let width = image.width
    let height = image.height
    let observations = detectText(in: url)
    var recognizedLines: [String] = []
    var totalArea = 0.0
    var leftArea = 0.0
    var rightArea = 0.0
    var topArea = 0.0
    var bottomArea = 0.0
    var largestArea = 0.0
    var weightedX = 0.0
    var weightedY = 0.0
    var wordCount = 0

    for observation in observations {
        if let text = observation.topCandidates(1).first?.string, !text.isEmpty {
            recognizedLines.append(text)
            wordCount += text.split { $0.isWhitespace }.count
        }
        let box = observation.boundingBox
        let area = Double(box.width * box.height)
        totalArea += area
        largestArea = max(largestArea, area)
        let centerX = Double(box.midX)
        let centerY = Double(box.midY)
        weightedX += centerX * area
        weightedY += centerY * area
        if centerX < 0.5 { leftArea += area } else { rightArea += area }
        if centerY < 0.5 { bottomArea += area } else { topArea += area }
    }

    let centerTextX = totalArea > 0 ? weightedX / totalArea : nil
    let centerTextY = totalArea > 0 ? weightedY / totalArea : nil

    return Metrics(
        path: path,
        width: width,
        height: height,
        averageLuminance: averageLuminance(for: image),
        textObservationCount: observations.count,
        wordCount: wordCount,
        recognizedLines: recognizedLines,
        textBoxAreaRatio: totalArea,
        leftTextAreaRatio: leftArea,
        rightTextAreaRatio: rightArea,
        topTextAreaRatio: topArea,
        bottomTextAreaRatio: bottomArea,
        largestBoxAreaRatio: largestArea,
        centerTextX: centerTextX,
        centerTextY: centerTextY
    )
}

let args = Array(CommandLine.arguments.dropFirst())
let metrics = args.map(collectMetrics)
let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
if let data = try? encoder.encode(metrics) {
    FileHandle.standardOutput.write(data)
}
