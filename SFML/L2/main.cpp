#include <SFML/Graphics.hpp>
#include <iostream>
int main()
{
    sf::RenderWindow window(sf::VideoMode(512, 512), "SFML Tutorial", sf::Style::Close | sf::Style::Titlebar | sf::Style::Resize);
    // 窗口大小 窗口标题 窗口style（调整大小 关闭等的键）
    while (window.isOpen())
    {
        sf::Event event;
        //事件
        while (window.pollEvent(event))
        {
            switch (event.type)
            {
            case sf::Event::Closed:
                window.close();
                break;
            case sf::Event::Resized:
                std::cout << "Width:" << event.size.width << "Height:" << event.size.height << std::endl;
                break;
            }
        }
    }
    return 0;
}