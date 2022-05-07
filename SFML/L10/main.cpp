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

    void update(int row, float delataTime, bool faceR)
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
        uvRect.top = currentImage.y * uvRect.height;
        if (faceR)
        {
            uvRect.left = currentImage.x * uvRect.width;
            uvRect.width = abs(uvRect.width);
        }
        else
        {
            uvRect.left = (currentImage.x + 1) * abs(uvRect.width);
            uvRect.width = -abs(uvRect.width);
        }
    };
    sf::IntRect uvRect;

private:
    sf::Vector2u imagecount;
    sf::Vector2u currentImage;

    float totalTime;
    float switchTime;
};

class Player
{
public:
    Player(sf::Texture *textrue, sf::Vector2u imageCount, float switchTime, float speed)
        : animation(textrue, imageCount, switchTime)
    {
        this->speed = speed;
        row = 3;
        faceRight = 1;

        body.setSize(sf::Vector2f(100.0f, 100.0f));
        body.setPosition(206.0f, 206.0f);
        body.setTexture(textrue);
    };
    ~Player(){};

    void update(float delataTime)
    {
        sf::Vector2f movement(0.0f, 0.0f);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::A))
            movement.x -= speed * delataTime;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::S))
            movement.y += speed * delataTime;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::D))
            movement.x += speed * delataTime;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::W))
            movement.y -= speed * delataTime;
        if (movement.x == 0.0f)
        {
            row = 0;
        }
        else
        {
            row = 1;
            if (movement.x > 0.0f)
                faceRight = 1;
            else
                faceRight = 0;
        }
        animation.update(row, delataTime, faceRight);
        body.setTextureRect(animation.uvRect);
        body.move(movement);
    };
    void Draw(sf::RenderWindow &window)
    {
        window.draw(body);
    };

private:
    sf::RectangleShape body;
    Animation animation;
    unsigned int row;
    float speed;
    bool faceRight;
};

int main()
{
    sf::RenderWindow window(sf::VideoMode(512, 512), "SFML Tutorial", sf::Style::Close | sf::Style::Titlebar | sf::Style::Resize);
    // 窗口大小 窗口标题 窗口style（调整大小 关闭等的键）

    sf::Texture playerTexture;
    playerTexture.loadFromFile("./linux.png");

    Player player(&playerTexture, sf::Vector2u(3, 8), 0.3f, 100.0f);

    float delataTime = 0.0f;
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

        player.update(delataTime);

        window.clear(sf::Color(150, 150, 150));
        player.Draw(window);
        window.display();
    }
    return 0;
}