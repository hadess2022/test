using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace julia
{
    internal static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }

        
    }

    class Gr
    {
        public void Form1_Paint(PaintEventArgs pe)
        {
            Image newImage = Image.FromFile("d802ec5b34b4209b3a53bd87660823e1c25f2977.png");
            PointF ulCorner = new PointF(100.0F, 100.0F);
            pe.Graphics.DrawImage(newImage, ulCorner);
        }
    }
}
