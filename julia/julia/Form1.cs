using System;
using System.Diagnostics.Eventing.Reader;
using System.Drawing;
using System.Windows.Forms;

namespace julia
{
    public partial class Form1 : Form
    {
        Bitmap bmp;
        public Form1()
        {
            InitializeComponent();
            
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            Iteration();
            GC.Collect();
        }

        public int GetColor(double x)
        {
            return Convert.ToInt32(x*x);
        }


        private void Iteration()
        {
            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            for (int i = -1 * pictureBox1.Width / 2 +1; i < pictureBox1.Width / 2; i++)
            {
                int x1=GetColor(i--);
                int x2=GetColor(i);
                for (int j = x1; j < x2; j++)
                {
                    if(j + (pictureBox1.Height) / 2>0 && j + (pictureBox1.Height / 2)< pictureBox1.Height)
                    bmp.SetPixel(i + (pictureBox1.Width / 2), j+ (pictureBox1.Height / 2), Color.Black);
                }
            }
            pictureBox1.Image = bmp;
            this.Refresh();
        }
    }
}
