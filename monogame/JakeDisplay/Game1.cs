using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace JakeDisplay;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;
    private Texture2D pic, pic2, pic3;
    private Rectangle picRec, picRec2, picRec3;

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        picRec = new Rectangle(0, 0, 272, 186);
        picRec2 = new Rectangle(300, 0, 300, 200);
        picRec3 = new Rectangle(0, 200, 233, 216);
        pic = Content.Load<Texture2D>("images");
        pic2 = Content.Load<Texture2D>("dexter");
        pic3 = Content.Load<Texture2D>("image");

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

        // TODO: Add your update logic here

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(Color.Plum);

        _spriteBatch.Begin();
        _spriteBatch.Draw(pic, picRec, Color.White);
        _spriteBatch.Draw(pic2, picRec2, Color.White);
        _spriteBatch.Draw(pic3, picRec3, Color.White);
        _spriteBatch.End();

        base.Draw(gameTime);
    }
}
