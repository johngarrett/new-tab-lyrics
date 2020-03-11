// swift-tools-version:5.0
import PackageDescription

let package = Package(
    name: "ntl-server",
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", .upToNextMinor(from: "3.3.0")),
        .package(url: "https://github.com/mongodb/mongo-swift-driver.git", from: "0.2.0")

    ],
    targets: [
        .target(name: "App", dependencies: ["Vapor", "MongoSwift"]),
        .target(name: "Run", dependencies: ["App"]),
        .testTarget(name: "AppTests", dependencies: ["App"]),
    ]
)

