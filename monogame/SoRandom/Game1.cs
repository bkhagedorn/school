using System;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace SoRandom;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;

    byte red = 0;
    byte green = 0;
    byte blue = 0;

    Color color;

    Random rand = new Random();

    GamePadState pad1, previousState;

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        Console.WriteLine("5/" + rand.Next(1, 32) + "/" + rand.Next(1901, 2001));

        int count = 0, num = -1;
        while (num != 2)
        {
            num = 0;
            num += rand.Next(1, 7);
            num += rand.Next(1, 7);
            count++;
        }
        Console.WriteLine(count);
        
        base.Initialize();
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        pad1 = GamePad.GetState(PlayerIndex.One);

        color = new Color(red, green, blue);

        if (pad1.IsButtonDown(Buttons.B) && previousState.IsButtonUp(Buttons.B))
            red += (byte)rand.Next(30, 80);
        if (pad1.IsButtonDown(Buttons.X) && previousState.IsButtonUp(Buttons.X))
            blue += (byte)rand.Next(30, 80);
        if (pad1.IsButtonDown(Buttons.A) && previousState.IsButtonUp(Buttons.A))
            green += (byte)rand.Next(30, 80);

        base.Update(gameTime);

        previousState = pad1;
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(color);

        base.Draw(gameTime);
    }
}
