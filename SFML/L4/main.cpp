#include <SFML/Graphics.hpp>
#include <iostream>
int main()
{
    sf::RenderWindow window(sf::VideoMode(512, 512), "SFML Tutorial", sf::Style::Close | sf::Style::Titlebar | sf::Style::Resize);
    // 窗口大小 窗口标题 窗口style（调整大小 关闭等的键）
    sf::RectangleShape player(sf::Vector2f(100.0f, 100.0f));
    player.setFillColor(sf::Color::Red);
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
            case sf::Event::TextEntered:
                if (event.text.unicode < 128)
                    printf("%c", event.text.unicode);
            }
        }
        window.draw(player);
        window.display();
    }
    return 0;
}