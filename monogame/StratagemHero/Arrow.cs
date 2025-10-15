using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Button;

public class Arrow
{
    private Texture2D _texture;
    private Color arrowColor = Color.White;
    private Keys direction;

    private List<Keys> badDirections = new List<Keys>();

    public Arrow(Texture2D _t, string d)
    {
        badDirections.Add(Keys.Left);
        badDirections.Add(Keys.Up);
        badDirections.Add(Keys.Down);
        badDirections.Add(Keys.Right);

        _texture = _t;
        if (d.Equals("left"))
        {
            direction = Keys.Left;
            badDirections.Remove(Keys.Left);
        }
        else if (d.Equals("right"))
        {
            direction = Keys.Right;
            badDirections.Remove(Keys.Right);
        }
        else if (d.Equals("up"))
        {
            direction = Keys.Up;
            badDirections.Remove(Keys.Up);
        }
        else if (d.Equals("down"))
        {
            direction = Keys.Down;
            badDirections.Remove(Keys.Down);   
        }

    }

    public Color getColor()
    {
        return arrowColor;
    }

    public void setColor(Color c)
    {
        arrowColor = c;
    }

    public Keys getDirection()
    {
        return direction;
    }

    public List<Keys> getBadDirections()
    {
        return badDirections;
    }

    public bool badKeyPressed(Keys key)
    {
        foreach (Keys i in badDirections)
        {
            if (key == i)
            {
                return true;
            }
        }
        return false;
    }

    public void setDirection(Keys k)
    {
        direction = k;
    }

    public Texture2D getTexture()
    {
        return _texture;
    }
}