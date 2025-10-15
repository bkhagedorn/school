using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace MovingWSpeed;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;
    private Texture2D bg, carLeft, carUp, carDown, carRight, currTexture;
    private Rectangle bgRect;
    private int x = 0, y = 0, speed = 2;

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        bgRect = new Rectangle(0, 0, 800, 500);

        base.Initialize();
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);

        bg = Content.Load<Texture2D>("city bird's eye view");
        carLeft = Content.Load<Texture2D>("carLeft");
        carUp = Content.Load<Texture2D>("carUp");
        carDown = Content.Load<Texture2D>("carDown");
        carRight = Content.Load<Texture2D>("carRight");
        currTexture = carRight;
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        KeyboardState keyboard = Keyboard.GetState();

        if (keyboard.IsKeyDown(Keys.Left))
        {
            x -= speed;
            currTexture = carLeft;
        }
        if (keyboard.IsKeyDown(Keys.Right))
        {
            x += speed;
            currTexture = carRight;
        }
        if (keyboard.IsKeyDown(Keys.Up))
        {
            y -= speed;
            currTexture = carUp;
        }
        if (keyboard.IsKeyDown(Keys.Down))
        {
            y += speed;
            currTexture = carDown;
        }

        if ((keyboard.IsKeyDown(Keys.F) && speed < 10) || (keyboard.IsKeyUp(Keys.Space) && speed < 2))
            speed++;
        if (keyboard.IsKeyUp(Keys.F) && speed > 2)
            speed--;
        if (keyboard.IsKeyDown(Keys.Space))
            speed = 0;

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(Color.CornflowerBlue);

        _spriteBatch.Begin();
        _spriteBatch.Draw(bg, bgRect, Color.White);
        _spriteBatch.Draw(currTexture, new Vector2(x, y), null, Color.White, 0.0f, Vector2.Zero, 0.25f, SpriteEffects.None, 0.0f);
        _spriteBatch.End();

        base.Draw(gameTime);
    }
}
