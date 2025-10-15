using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Button;
using System.Collections.Generic;
using Code;
using System;

namespace StratagemHero;

public class Game1 : Game
{
    private GraphicsDeviceManager _graphics;
    private SpriteBatch _spriteBatch;
    private SpriteFont _font, _fontBig;
    private Texture2D _arrowLeft, _arrowRight, _arrowUp, _arrowDown;
    private Random rand = new Random();

    private int count = 0, listCount = 0, score = 0, failTimer = 0, xCheck = 100, timer = 10, countdown = 60, round = 1, intermissionTimer = 180;

    private string screen = "start";

    private bool flag = false; // When there were two of the same arrow in a row, one button press would active both, this stops that from happening
    private bool done = false, perfect = true;

    private List<StratagemCode> stratagemList = new List<StratagemCode>(), randList = new List<StratagemCode>(); // I spent 20 minutes struggling with this

    public Game1()
    {
        _graphics = new GraphicsDeviceManager(this);
        Content.RootDirectory = "Content";
        IsMouseVisible = true;

    }

    protected override void Initialize()
    {
        base.Initialize();
    }

    protected override void LoadContent()
    {
        _spriteBatch = new SpriteBatch(GraphicsDevice);
        _font = Content.Load<SpriteFont>("font");
        _fontBig = Content.Load<SpriteFont>("fontBig");
        _arrowLeft = Content.Load<Texture2D>("images/arrowLeft");
        _arrowRight = Content.Load<Texture2D>("images/arrowRight");
        _arrowUp = Content.Load<Texture2D>("images/arrowUp");
        _arrowDown = Content.Load<Texture2D>("images/arrowDown");

        // :(
        // mission
        StratagemCode reinforce = new StratagemCode("reinforce", new Arrow[] { createArrow("up"), createArrow("down"), createArrow("right"), createArrow("left"), createArrow("up") });
        StratagemCode sosBeacon = new StratagemCode("sosBeacon", new Arrow[] { createArrow("up"), createArrow("down"), createArrow("right"), createArrow("up") });
        StratagemCode resupply = new StratagemCode("resupply", new Arrow[] { createArrow("down"), createArrow("down"), createArrow("right"), createArrow("up") });
        StratagemCode eagleRearm = new StratagemCode("eagleRearm", new Arrow[] { createArrow("up"), createArrow("up"), createArrow("left"), createArrow("up"), createArrow("right") });
        StratagemCode sssdDelivery = new StratagemCode("sssdDelivery", new Arrow[] { createArrow("down"), createArrow("down"), createArrow("down"), createArrow("up"), createArrow("up") });
        StratagemCode prospectingDrill = new StratagemCode("prospectingDrill", new Arrow[] { createArrow("down"), createArrow("down"), createArrow("left"), createArrow("right"), createArrow("down"), createArrow("down") });
        StratagemCode superEarthFlag = new StratagemCode("superEarthFlag", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("down"), createArrow("up") });
        StratagemCode hellbomb = new StratagemCode("hellbomb", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("left"), createArrow("down"), createArrow("up"), createArrow("right"), createArrow("down"), createArrow("up") });
        StratagemCode uploadData = new StratagemCode("sssdDelivery", new Arrow[] { createArrow("left"), createArrow("right"), createArrow("up"), createArrow("up"), createArrow("up") });
        StratagemCode seismicProbe = new StratagemCode("seismicProbe", new Arrow[] { createArrow("up"), createArrow("up"), createArrow("left"), createArrow("right"), createArrow("down"), createArrow("down") });
        StratagemCode orbitalFlare = new StratagemCode("orbitalFlare", new Arrow[] { createArrow("right"), createArrow("right"), createArrow("left"), createArrow("left") });
        StratagemCode seafArtillery = new StratagemCode("seafArtillery", new Arrow[] { createArrow("right"), createArrow("up"), createArrow("up"), createArrow("down") });
        StratagemCode fluidVessel = new StratagemCode("fluidVessel", new Arrow[] { createArrow("up"), createArrow("left"), createArrow("right"), createArrow("down"), createArrow("up"), createArrow("up") });
        StratagemCode tectonicDrill = new StratagemCode("prospectingDrill", new Arrow[] { createArrow("up"), createArrow("down"), createArrow("up"), createArrow("down"), createArrow("up"), createArrow("down") });
        StratagemCode hiveDrill = new StratagemCode("prospectingDrill", new Arrow[] { createArrow("left"), createArrow("up"), createArrow("down"), createArrow("right"), createArrow("down"), createArrow("down") });

        randList.Add(reinforce);
        randList.Add(sosBeacon);
        randList.Add(resupply);
        randList.Add(eagleRearm);
        randList.Add(sssdDelivery);
        randList.Add(prospectingDrill);
        randList.Add(superEarthFlag);
        randList.Add(hellbomb);
        randList.Add(uploadData);
        randList.Add(seismicProbe);
        randList.Add(orbitalFlare);
        randList.Add(seafArtillery);
        randList.Add(fluidVessel);
        randList.Add(tectonicDrill);
        randList.Add(hiveDrill);

        // warbond
        StratagemCode sterilizer = new StratagemCode("sterilizer", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("up"), createArrow("down"), createArrow("left") });
        StratagemCode guardDogBreath = new StratagemCode("guardDogBreath", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("left"), createArrow("up"), createArrow("right"), createArrow("up") });
        StratagemCode directionalShield = new StratagemCode("directionalShield", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("left"), createArrow("right"), createArrow("up"), createArrow("up") });
        StratagemCode antiTankEMP = new StratagemCode("antiTankEMP", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("left"), createArrow("right"), createArrow("right"), createArrow("right") });
        StratagemCode flameSentry = new StratagemCode("flameSentry", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("right"), createArrow("down"), createArrow("up"), createArrow("up") });
        StratagemCode portableHellbomb = new StratagemCode("portableHellbomb", new Arrow[] { createArrow("down"), createArrow("right"), createArrow("up"), createArrow("up"), createArrow("up") });
        StratagemCode hoverPack = new StratagemCode("hoverPack", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("up"), createArrow("down"), createArrow("left"), createArrow("right") });
        StratagemCode oneTrueFlag = new StratagemCode("oneTrueFlag", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("right"), createArrow("right"), createArrow("up") });
        StratagemCode deEscalator = new StratagemCode("deEscalator", new Arrow[] { createArrow("down"), createArrow("right"), createArrow("up"), createArrow("left"), createArrow("right") });
        StratagemCode guardK9 = new StratagemCode("guardK9", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("left"), createArrow("up"), createArrow("right"), createArrow("left") });
        StratagemCode epoch = new StratagemCode("epoch", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("up"), createArrow("left"), createArrow("right") });
        StratagemCode laserSentry = new StratagemCode("laserSentry", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("right"), createArrow("down"), createArrow("up"), createArrow("right") });
        StratagemCode warpPack = new StratagemCode("warpPack", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("right"), createArrow("down"), createArrow("left"), createArrow("right") });
        StratagemCode speargun = new StratagemCode("speargun", new Arrow[] { createArrow("down"), createArrow("right"), createArrow("down"), createArrow("left"), createArrow("up"), createArrow("right") });
        StratagemCode expendableNapalm = new StratagemCode("expendableNapalm", new Arrow[] { createArrow("down"), createArrow("down"), createArrow("left"), createArrow("up"), createArrow("left") });
        StratagemCode soloSilo = new StratagemCode("soloSilo", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("right"), createArrow("down"), createArrow("down") });

        randList.Add(sterilizer);
        randList.Add(guardDogBreath);
        randList.Add(directionalShield);
        randList.Add(antiTankEMP);
        randList.Add(flameSentry);
        randList.Add(portableHellbomb);
        randList.Add(hoverPack);
        randList.Add(oneTrueFlag);
        randList.Add(deEscalator);
        randList.Add(guardK9);
        randList.Add(epoch);
        randList.Add(laserSentry);
        randList.Add(warpPack);
        randList.Add(speargun);
        randList.Add(expendableNapalm);
        randList.Add(soloSilo);

        // lvl 1
        StratagemCode machineGun = new StratagemCode("machineGun", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("down"), createArrow("up"), createArrow("right") });
        StratagemCode antiMatRifle = new StratagemCode("antiMatRifle", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("right"), createArrow("up"), createArrow("down") });
        StratagemCode stalwart = new StratagemCode("stalwart", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("down"), createArrow("up"), createArrow("up"), createArrow("left") });
        StratagemCode orbitalGatlingBarrage = new StratagemCode("orbitalGatlingBarrage", new Arrow[] { createArrow("right"), createArrow("down"), createArrow("left"), createArrow("up"), createArrow("up") });
        StratagemCode eagleStrafingRun = new StratagemCode("eagleStrafingRun", new Arrow[] { createArrow("up"), createArrow("right"), createArrow("right") });
        StratagemCode eagleAirstrike = new StratagemCode("eagleAirstrike", new Arrow[] { createArrow("up"), createArrow("right"), createArrow("down"), createArrow("right") });
        StratagemCode orbitalPrecisionStrike = new StratagemCode("orbitalPrecisionStrike", new Arrow[] { createArrow("right"), createArrow("right"), createArrow("up") });
        StratagemCode orbitalGasStrike = new StratagemCode("orbitalGasStrike", new Arrow[] { createArrow("right"), createArrow("right"), createArrow("down"), createArrow("right") });
        StratagemCode antiPersMinefield = new StratagemCode("antiPersMinefield", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("up"), createArrow("right") });
        StratagemCode supplyPack = new StratagemCode("supplyPack", new Arrow[] { createArrow("down"), createArrow("left"), createArrow("down"), createArrow("up"), createArrow("up"), createArrow("down") });
        StratagemCode machineGunSentry = new StratagemCode("machineGunSentry", new Arrow[] { createArrow("down"), createArrow("up"), createArrow("right"), createArrow("right"), createArrow("up") });

        randList.Add(machineGun);
        randList.Add(antiMatRifle);
        randList.Add(stalwart);
        randList.Add(orbitalGatlingBarrage);
        randList.Add(eagleStrafingRun);
        randList.Add(eagleAirstrike);
        randList.Add(orbitalPrecisionStrike);
        randList.Add(orbitalGasStrike);
        randList.Add(antiPersMinefield);
        randList.Add(supplyPack);
        randList.Add(machineGunSentry);

        stratagemList = RandomizeList(4);
    }

    protected Arrow createArrow(string str)
    {
        if (str.Equals("left"))
            return new Arrow(_arrowLeft, "left");
        else if (str.Equals("up"))
            return new Arrow(_arrowUp, "up");
        else if (str.Equals("down"))
            return new Arrow(_arrowDown, "down");
        else
            return new Arrow(_arrowRight, "right");
    }

    protected List<StratagemCode> RandomizeList(int x)
    {
        List<StratagemCode> temp = new List<StratagemCode>();
        for (int i = 0; i < x; i++)
        {
            temp.Add(randList[rand.Next(randList.Count)]);
        }
        return temp;
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        if (screen.Equals("start") || screen.Equals("end"))
        {
            if (Keyboard.GetState().IsKeyDown(Keys.Left) || Keyboard.GetState().IsKeyDown(Keys.Right) || Keyboard.GetState().IsKeyDown(Keys.Up) || Keyboard.GetState().IsKeyDown(Keys.Down))
            {
                screen = "intermission";
                flag = true;
            }

            if (screen.Equals("end"))
            {
                round = 1;
                timer = 10;
                countdown = 60;
                listCount = 0;
                count = 0;
                score = 0;
                stratagemList = RandomizeList(4);
            }
        }

        if (screen.Equals("game"))
        {
            if (!done)
            {
                if (failTimer == 0 && timer != 0)
                {
                    if (Keyboard.GetState().IsKeyDown(stratagemList[listCount].getCode()[count].getDirection()) && !flag)
                    {
                        flag = true;
                        score += 50;
                        stratagemList[listCount].getCode()[count].setColor(Microsoft.Xna.Framework.Color.Yellow);
                        if (count < stratagemList[listCount].getCode().Length - 1)
                            count++;
                        else
                        {
                            for (int i = 0; i < stratagemList[listCount].getCode().Length; i++)
                            {
                                stratagemList[listCount].getCode()[i].setColor(Microsoft.Xna.Framework.Color.White);
                            }
                            count = 0;
                            score += 500;
                            timer++;
                            if (listCount != stratagemList.Count - 1)
                            {
                                listCount++;
                            }
                            else
                            {
                                stratagemList = RandomizeList(4 + round);
                                countdown = 60;
                                listCount = 0;
                                score += round * 100;
                                score += timer * 150;
                                if (perfect)
                                    score += 1000;
                                round++;
                                screen = "score";
                            }        
                        }
                    }
                    foreach (Keys key in Keyboard.GetState().GetPressedKeys())
                    {
                        if (stratagemList[listCount].getCode()[count].badKeyPressed(key) && !flag)
                        {
                            flag = true;
                            foreach (Arrow obj in stratagemList[listCount].getCode())
                            {
                                obj.setColor(Microsoft.Xna.Framework.Color.White);
                            }
                            count = 0;
                            score -= 350;
                            failTimer = 60;
                            perfect = false;
                        }
                    }

                    if (timer != 0)
                    {
                        if (countdown > 0)
                            countdown--;
                        else
                        {
                            timer--;
                            countdown = 60;
                        }
                    }
                    else if (timer > 10)
                        timer = 10;
                }
                else
                    failTimer--;

            }
        }
        if (Keyboard.GetState().GetPressedKeys().Length == 0)
            flag = false;

        if (screen.Equals("intermission") || screen.Equals("score"))
        {
            if (intermissionTimer > 0)
                intermissionTimer--;
            else
            {
                intermissionTimer = 180;
                timer = 10;
                perfect = true;
                if (screen.Equals("intermission"))
                    screen = "game";
                else
                    screen = "intermission";
            }
        }

        if (timer == 0)
            screen = "end";

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(Microsoft.Xna.Framework.Color.Black);

        _spriteBatch.Begin();

        if (screen.Equals("start"))
        {
            _spriteBatch.DrawString(_fontBig, "Stratagem Hero", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 400) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _fontBig.MeasureString("Stratagem Hero") * 0.5f, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_font, "Enter any stratagem input to start", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 475) * 0.5f, Microsoft.Xna.Framework.Color.Yellow, 0.0f, _font.MeasureString("Enter any stratagem input to start") * 0.5f, 1f, SpriteEffects.None, 0.0f);
        }

        if (screen.Equals("intermission"))
        {
            _spriteBatch.DrawString(_fontBig, "ROUND " + round, new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 400) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _fontBig.MeasureString("ROUND  ") * 0.5f, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_font, "Ready?", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 475) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _font.MeasureString("Ready?") * 0.5f, 1f, SpriteEffects.None, 0.0f);
        }

        if (screen.Equals("end"))
        {
            _spriteBatch.DrawString(_fontBig, "GAME OVER", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 250) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _fontBig.MeasureString("GAME OVER") * 0.5f, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_fontBig, "YOUR FINAL SCORE", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 350) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _fontBig.MeasureString("YOUR FINAL SCORE") * 0.5f, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_fontBig, score.ToString(), new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 450) * 0.5f, Microsoft.Xna.Framework.Color.White, 0.0f, _fontBig.MeasureString(score.ToString()) * 0.5f, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_font, "Enter any stratagem input to restart", new Vector2(GraphicsDevice.PresentationParameters.BackBufferWidth, 550) * 0.5f, Microsoft.Xna.Framework.Color.Yellow, 0.0f, _font.MeasureString("Enter any stratagem input to restart") * 0.5f, 1f, SpriteEffects.None, 0.0f);
        }

        if (screen.Equals("score"))
        {
            _spriteBatch.DrawString(_fontBig, "LEVEL BONUS: " + round * 100, new Vector2(50, 250), Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_fontBig, "TIME BONUS: " + timer * 15, new Vector2(50, 300), Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
            if (perfect)
                _spriteBatch.DrawString(_fontBig, "PERFECT BONUS: 1000", new Vector2(50, 350), Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
            else
                _spriteBatch.DrawString(_fontBig, "PERFECT BONUS: 0", new Vector2(50, 350), Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
            _spriteBatch.DrawString(_fontBig, "CURRENT SCORE: " + score, new Vector2(50, 400), Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
        }

        if (screen.Equals("game"))
        {
            _spriteBatch.DrawString(_font, "Score: " + score, Vector2.Zero, Microsoft.Xna.Framework.Color.White);
            if (timer > 3)
                _spriteBatch.Draw(Content.Load<Texture2D>("images/box"), new Vector2(50, 375), null, Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, new Vector2(0.2f * timer, 0.15f), SpriteEffects.None, 0.0f);
            else
                _spriteBatch.Draw(Content.Load<Texture2D>("images/box"), new Vector2(50, 375), null, Microsoft.Xna.Framework.Color.Red, 0.0f, Vector2.Zero, new Vector2(0.2f * timer, 0.15f), SpriteEffects.None, 0.0f);
            for (int i = listCount; i < stratagemList.Count; i++)
            {
                if (i == listCount)
                {
                    _spriteBatch.Draw(Content.Load<Texture2D>("images/" + stratagemList[i].getName()), new Vector2(xCheck, 80), null, Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 1f, SpriteEffects.None, 0.0f);
                    xCheck += 148;
                }
                else
                {
                    _spriteBatch.Draw(Content.Load<Texture2D>("images/" + stratagemList[i].getName()), new Vector2(xCheck - 25, 122.5f), null, Microsoft.Xna.Framework.Color.White, 0.0f, Vector2.Zero, 0.65f, SpriteEffects.None, 0.0f);
                    xCheck += 80;
                }
            }
            xCheck = 100;
            if (failTimer == 0)
            {
                for (int i = 0; i < stratagemList[listCount].getCode().Length; i++)
                {
                    _spriteBatch.Draw(stratagemList[listCount].getCode()[i].getTexture(), new Vector2(80 * (i + 1), 250), null, stratagemList[listCount].getCode()[i].getColor(), 0.0f, Vector2.Zero, 0.25f, SpriteEffects.None, 0.0f);
                }
            }
            else
            {
                for (int i = 0; i < stratagemList[listCount].getCode().Length; i++)
                {
                    _spriteBatch.Draw(stratagemList[listCount].getCode()[i].getTexture(), new Vector2(80 * (i + 1), 250), null, Microsoft.Xna.Framework.Color.Red, 0.0f, Vector2.Zero, 0.25f, SpriteEffects.None, 0.0f);
                }
            }
        }
        _spriteBatch.End();

        base.Draw(gameTime);
    }
}
