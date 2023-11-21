#include <iostream>
#include <gumbo.h>

void parseHtml(const std::string& html) {
    GumboOutput* output = gumbo_parse(html.c_str());
    std::cout << "Parsed HTML:\n" << output->root->v.text << std::endl;
    gumbo_destroy_output(&kGumboDefaultOptions, output);
}

int main() {
    httplib::Client client("https://www.scrapethissite.com/pages/simple/");

    auto req = client.Get("/");

    if (res && res->status==200) {
        std::cout << "Received HTML:\n" << res->body << std::endl;
        parseHtml(res->body);
    } else {
        std::cerr << "Request Failed"
    }

    return 0;
}