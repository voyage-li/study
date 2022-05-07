#include <SFML/Graphics.hpp>
#include <iostream>
//没有例化
class Collision
{
public:
    Collision(sf::RectangleShape &body)
        : body(body){

          };
    ~Collision(){

    };

    bool check(Collision &other, float push)
    {
        sf::Vector2f other_pos = other.getpos();
        sf::Vector2f other_half_size = other.gethalfsize();

        sf::Vector2f this_pos = getpos();
        sf::Vector2f this_half_size = gethalfsize();

        float deltax = other_pos.x - this_pos.x;
        float deltay = other_pos.y - this_pos.y;

        float intersectx = abs(deltax) - (other_half_size.x + this_half_size.x);
        float intersecty = abs(deltay) - (other_half_size.y + this_half_size.y);

        if (intersectx < 0.0f && intersecty < 0.0f)
        {
            push = std::max(std::max(push, 0.0f), 1.0f);

            if (intersectx > intersecty)
            {
                if (deltax > 0.0f)
                {
                    move(intersectx * (1.0f - push), 0.0f);
                    other.move(-intersectx * push, 0.0f);
                }
                else
                {
                    move(-intersectx * (1.0f - push), 0.0f);
                    other.move(intersecty * push, 0.0f);
                }
            }
            else
            {
                if (deltay > 0.0f)
                {
                    move(0.0f, intersecty * (1.0f - push));
                    other.move(0.0f, -intersecty * push);
                }
                else
                {
                    move(0.0f, -intersecty * (1.0f - push));
                    other.move(0.0f, intersecty * push);
                }
            }

            return true;
        }

        return false;
    };

    void move(float dx, float dy){

    };

    sf::Vector2f getpos()
    {
        return body.getPosition();
    };

    sf::Vector2f gethalfsize()
    {
        return body.getSize() / 2.0f;
    };

private:
    sf::RectangleShape &body;
};