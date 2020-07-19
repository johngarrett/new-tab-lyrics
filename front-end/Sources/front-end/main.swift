import HyperSwift
import Foundation

let htmlOutput = URL(fileURLWithPath: "/Users/garrepi/temp/ntl.html")

let page = HTMLComponent {
    VStack("") {
        Paragraph("\"It'll be alright, it'll be alright, it'll be alright\"")
            .font(weight: "bold", size: 45, family: "sans-serif")
        HStack("", justify: .flexEnd) {
            VStack("") {
                Paragraph("- Car Seat Headrest")
                    .font(weight: "normal", size: 16, family: "sans-serif")
                    .color(CSSColor("#A4A4A4"))
                Paragraph("Cosmic Hero @3:40")
                    .font(weight: "normal", size: 14, family: "sans-serif")
                    .color(CSSColor("#A1A1A1"))
            }.padding(right: 20)
            Image(url: "https://i.guim.co.uk/img/media/8f209eb1947375add6e92cfe23aea4e61b8677cd/0_107_5760_3456/master/5760.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=606e8ef52c8d20545b2057e30de6f610")
                .width(100)
                .height(100)
        }
    }
    .margin(10, .percent)
}
try page.render().write(to: htmlOutput, atomically: true, encoding: String.Encoding.utf8)
