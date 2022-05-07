#include <SFML/Graphics.hpp>
#include <iostream>
// 图像抖动是因为截图的问题
class Animation
{
public:
    Animation(sf::Texture *textrue, sf::Vector2u imageCount, float switchTime)
    {
        this->imagecount = imageCount;
        this->switchTime = switchTime;
        totalTime = 0.0f;
        currentImage.x = 0;
        uvRect.width = textrue->getSize().x / (float)(imagecount.x);
        uvRect.height = textrue->getSize().y / (float)(imagecount.y);
    };
    ~Animation(){

    };

    void update(int row, float delataTime)
    {
        currentImage.y = row;
        totalTime += delataTime;
        if (totalTime >= switchTime)
        {
            totalTime -= switchTime;
            currentImage.x++;
            if (currentImage.x >= imagecount.x)
            {
                currentImage.x = 0;
            }
        }
        uvRect.left = currentImage.x * uvRect.width;
        uvRect.top = currentImage.y * uvRect.height;
    };
    sf::IntRect uvRect;

private:
    sf::Vector2u imagecount;
    sf::Vector2u currentImage;

    float totalTime;
    float switchTime;
};

int main()
{
    sf::RenderWindow window(sf::VideoMode(512, 512), "SFML Tutorial", sf::Style::Close | sf::Style::Titlebar | sf::Style::Resize);
    // 窗口大小 窗口标题 窗口style（调整大小 关闭等的键）
    sf::RectangleShape player(sf::Vector2f(100.0f, 100.0f));
    player.setPosition(206.0f, 206.0f);
    sf::Texture playerTexture;
    playerTexture.loadFromFile("./linux.png");
    player.setTexture(&playerTexture);

    Animation animation(&playerTexture, sf::Vector2u(3, 8), 1.0f);

    float delataTime;
    sf::Clock clock;

    while (window.isOpen())
    {
        delataTime = clock.restart().asSeconds();
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

        animation.update(3, delataTime);
        player.setTextureRect(animation.uvRect);

        window.clear(sf::Color(150, 150, 150));
        window.draw(player);
        window.display();
    }
    return 0;
}