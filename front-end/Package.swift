// swift-tools-version:5.2

import PackageDescription

let package = Package(
    name: "front-end",
    dependencies: [
        .package(url: "https://www.github.com/johngarrett/HyperSwift", .branch("master"))
    ],
    targets: [
        .target(name: "front-end", dependencies: ["HyperSwift"])
    ]
)
