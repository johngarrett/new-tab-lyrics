import XCTest

#if !canImport(ObjectiveC)
public func allTests() -> [XCTestCaseEntry] {
    return [
        testCase(new_tab_lyricsTests.allTests),
    ]
}
#endif
