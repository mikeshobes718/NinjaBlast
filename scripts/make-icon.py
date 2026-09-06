#!/usr/bin/env python3
from AppKit import (
    NSBitmapImageRep,
    NSCalibratedRGBColorSpace,
    NSColor,
    NSBezierPath,
    NSGraphicsContext,
    NSImage,
    NSBitmapImageFileTypePNG,
    NSFont,
    NSMutableParagraphStyle,
    NSFontAttributeName,
    NSForegroundColorAttributeName,
    NSParagraphStyleAttributeName,
    NSCenterTextAlignment,
)
from Foundation import NSMakeRect, NSAttributedString, NSURL
import os

size = 1024
scale = 2
rep = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(
    None, size, size, 8, 4, True, False, NSCalibratedRGBColorSpace, 0, 0
)
rep.setSize_((size, size))
ctx = NSGraphicsContext.graphicsContextWithBitmapImageRep_(rep)
NSGraphicsContext.setCurrentContext_(ctx)

NSColor.colorWithCalibratedRed_green_blue_alpha_(0.06, 0.06, 0.07, 1.0).setFill()
NSBezierPath.fillRect_(NSMakeRect(0, 0, size, size))

red = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.882, 0.024, 0.0, 1.0)
white = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.96, 0.96, 0.97, 1.0)
purple = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.62, 0.32, 0.92, 1.0)

cx, cy = size / 2, size / 2

# Base
red.setFill()
base = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(
    NSMakeRect(cx - 210, 210, 420, 170), 48, 48
)
base.fill()

# LED
purple.setFill()
led = NSBezierPath.bezierPathWithOvalInRect_(NSMakeRect(cx - 18, 318, 36, 36))
led.fill()

# Cup
white.setStroke()
cup = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(
    NSMakeRect(cx - 150, 390, 300, 340), 36, 36
)
cup.setLineWidth_(22)
cup.stroke()

# Sip lid
white.setFill()
lid = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(
    NSMakeRect(cx - 90, 720, 180, 70), 28, 28
)
lid.fill()

# Straw / sip
straw = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(
    NSMakeRect(cx - 18, 780, 36, 90), 12, 12
)
straw.fill()

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(root, "Blast/Assets.xcassets/AppIcon.appiconset/AppIcon.png")
data = rep.representationUsingType_properties_(NSBitmapImageFileTypePNG, None)
data.writeToFile_atomically_(out, True)
print(out)
