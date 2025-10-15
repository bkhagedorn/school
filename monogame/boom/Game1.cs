using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace boom;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;
    private Texture2D _texture;

    private byte redIntensity = 0;
    private bool increase = true;

    private Queue<System.Numerics.Vector2> _inputBufferX;
    private Queue<System.Numerics.Vector2> _inputBufferY;
    private const int MAX_BUFFER_SIZE = 2;
    private System.Numerics.Vector2 _position = new System.Numerics.Vector2(0, 0);
    private int _speed = 5;

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        base.Initialize();
        _inputBufferX = new Queue<System.Numerics.Vector2>(MAX_BUFFER_SIZE);
        _inputBufferY = new Queue<System.Numerics.Vector2>(MAX_BUFFER_SIZE);
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);
        _texture = new Texture2D(GraphicsDevice, 1, 1);
        _texture.SetData(new Color[] { Color.White });
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        System.Numerics.Vector2 newDirectionX = System.Numerics.Vector2.Zero;
        System.Numerics.Vector2 newDirectionY = System.Numerics.Vector2.Zero;

        if (increase)
            redIntensity++;
        else
            redIntensity--;

        if (redIntensity == 250)
            increase = false;
        else if (redIntensity == 10)
            increase = true;

        if (Keyboard.GetState().IsKeyDown(Keys.Left))
            newDirectionX = -System.Numerics.Vector2.UnitX;
        if (Keyboard.GetState().IsKeyDown(Keys.Right))
            newDirectionX = System.Numerics.Vector2.UnitX;
        if (Keyboard.GetState().IsKeyDown(Keys.Down))
            newDirectionY = System.Numerics.Vector2.UnitY;
        if (Keyboard.GetState().IsKeyDown(Keys.Up))
            newDirectionY = -System.Numerics.Vector2.UnitY;

        if (newDirectionX != System.Numerics.Vector2.Zero && _inputBufferX.Count < MAX_BUFFER_SIZE)
            _inputBufferX.Enqueue(newDirectionX);
        if (newDirectionY != System.Numerics.Vector2.Zero && _inputBufferY.Count < MAX_BUFFER_SIZE)
            _inputBufferY.Enqueue(newDirectionY);

        if (_inputBufferX.Count > 0)
        {
            System.Numerics.Vector2 nextDirection = _inputBufferX.Dequeue();
            _position += nextDirection * _speed;
        }
        if (_inputBufferY.Count > 0)
        {
            System.Numerics.Vector2 nextDirection = _inputBufferY.Dequeue();
            _position += nextDirection * _speed;
        }

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(new Color(redIntensity, 0, 0));

        _spriteBatch.Begin();
        _spriteBatch.Draw(_texture, new Rectangle((int)_position.X, (int)_position.Y, 50, 50), Color.White);
        _spriteBatch.End();

        base.Draw(gameTime);
    }
}
