#include <SFML/Graphics.hpp>
#include <iostream>
int main()
{
    sf::RenderWindow window(sf::VideoMode(512, 512), "SFML Tutorial", sf::Style::Close | sf::Style::Titlebar | sf::Style::Resize);
    // 窗口大小 窗口标题 窗口style（调整大小 关闭等的键）
    sf::RectangleShape player(sf::Vector2f(100.0f, 100.0f));
    player.setPosition(206.0f, 206.0f);
    sf::Texture playerTexture;
    playerTexture.loadFromFile("./linux.png");
    player.setTexture(&playerTexture);
    // player.setFillColor(sf::Color::Red);
    // player.setOrigin(50.0f, 50.0f);
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
            }
        }

        window.clear();
        window.draw(player);
        window.display();
    }
    return 0;
}