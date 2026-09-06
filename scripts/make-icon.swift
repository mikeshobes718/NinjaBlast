import AppKit

let size = 1024
let rep = NSBitmapImageRep(
    bitmapDataPlanes: nil,
    pixelsWide: size,
    pixelsHigh: size,
    bitsPerSample: 8,
    samplesPerPixel: 4,
    hasAlpha: true,
    isPlanar: false,
    colorSpaceName: .deviceRGB,
    bytesPerRow: 0,
    bitsPerPixel: 0
)!
rep.size = NSSize(width: size, height: size)

NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)

func fill(_ color: NSColor, _ rect: NSRect, radius: CGFloat = 0) {
    color.setFill()
    if radius > 0 {
        NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius).fill()
    } else {
        NSBezierPath.fill(rect)
    }
}

fill(NSColor(calibratedRed: 0.06, green: 0.06, blue: 0.07, alpha: 1), NSRect(x: 0, y: 0, width: size, height: size))

let red = NSColor(calibratedRed: 0.882, green: 0.024, blue: 0, alpha: 1)
let white = NSColor(calibratedRed: 0.96, green: 0.96, blue: 0.97, alpha: 1)
let purple = NSColor(calibratedRed: 0.62, green: 0.32, blue: 0.92, alpha: 1)
let cx = CGFloat(size) / 2
let stroke: CGFloat = 28

fill(red, NSRect(x: cx - 200, y: 228, width: 400, height: 168), radius: 44)
fill(purple, NSRect(x: cx - 16, y: 332, width: 32, height: 32), radius: 16)

let cupWidth: CGFloat = 292
let cupLeft = cx - cupWidth / 2
let cupBottom: CGFloat = 388
let cupHeight: CGFloat = 318
let cupRight = cupLeft + cupWidth
let cupTop = cupBottom + cupHeight

white.setStroke()
white.setFill()

let cup = NSBezierPath()
cup.lineWidth = stroke
cup.lineCapStyle = .round
cup.lineJoinStyle = .round
cup.move(to: NSPoint(x: cupLeft, y: cupTop - 8))
cup.line(to: NSPoint(x: cupLeft, y: cupBottom + 36))
cup.appendArc(
    withCenter: NSPoint(x: cupLeft + 36, y: cupBottom + 36),
    radius: 36,
    startAngle: 180,
    endAngle: 270
)
cup.line(to: NSPoint(x: cupRight - 36, y: cupBottom))
cup.appendArc(
    withCenter: NSPoint(x: cupRight - 36, y: cupBottom + 36),
    radius: 36,
    startAngle: 270,
    endAngle: 360
)
cup.line(to: NSPoint(x: cupRight, y: cupTop - 8))
cup.stroke()

let lidHeight: CGFloat = 78
let lidRect = NSRect(x: cupLeft - 10, y: cupTop - 24, width: cupWidth + 20, height: lidHeight)
fill(white, lidRect, radius: 30)

let sipWidth: CGFloat = 86
let sipHeight: CGFloat = 52
fill(white, NSRect(x: cx - sipWidth / 2, y: lidRect.maxY - 10, width: sipWidth, height: sipHeight), radius: 20)

NSGraphicsContext.restoreGraphicsState()

guard let png = rep.representation(using: .png, properties: [:]) else {
    fputs("failed to encode png\n", stderr)
    exit(1)
}

let url = URL(fileURLWithPath: CommandLine.arguments[1])
try png.write(to: url)
print(url.path)
