using Button;
using Microsoft.Xna.Framework.Graphics;

namespace Code;

public class StratagemCode
{
    private string name;

    private Arrow[] code;

    public StratagemCode(string n, Arrow[] c)
    {
        name = n;
        code = c;
    }

    public string getName()
    {
        return name;
    }

    public Arrow[] getCode()
    {
        return code;
    }
}