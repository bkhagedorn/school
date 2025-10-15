using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Moodlight;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;

    Color currColor = Color.Black;

    bool gameOver = false;

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        // TODO: Add your initialization logic here

        base.Initialize();
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);

        // TODO: use this.Content to load your game content here
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        GamePadState pad1 = GamePad.GetState(PlayerIndex.One);

        if (pad1.IsButtonDown(Buttons.B))
            currColor = Color.Red;
        else if (pad1.Triggers.Left > 0)
            currColor = Color.Orange;
        else if (pad1.IsButtonDown(Buttons.Y))
            currColor = Color.Yellow;
        else if (pad1.IsButtonDown(Buttons.A))
            currColor = Color.Green;
        else if (pad1.IsButtonDown(Buttons.X))
            currColor = Color.Blue;
        else if (pad1.Triggers.Right > 0)
            currColor = Color.Indigo;
        else if (pad1.ThumbSticks.Left.X < 0)
            currColor = Color.Violet;
        else if (pad1.ThumbSticks.Left.Y > 0)
            currColor = Color.PapayaWhip;
        else if (pad1.ThumbSticks.Left.Y < 0)
            currColor = Color.Lime;
        else if (pad1.ThumbSticks.Left.X > 0)
            currColor = Color.LightSeaGreen;
        else if (pad1.IsButtonDown(Buttons.Start))
            currColor = Color.Salmon;

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        Color backgroundColor = currColor;
        if (!gameOver)
            GraphicsDevice.Clear(backgroundColor);
        else
            GraphicsDevice.Clear(Color.Black);

        // TODO: Add your drawing code here

            base.Draw(gameTime);
    }
    // Brought to you by Alexander the Great
}
