using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace GraphsLeague
{
    public partial class formMain : Form
    {

        public string userName;
        public string server; 
        public formMain()
        {
            InitializeComponent();
            comboBoxServer.Items.Add("br");
            comboBoxServer.Items.Add("eune");
            comboBoxServer.Items.Add("euw");
            comboBoxServer.Items.Add("jp");
            comboBoxServer.Items.Add("kr");
            comboBoxServer.Items.Add("lan");
            comboBoxServer.Items.Add("las");
            comboBoxServer.Items.Add("na");
            comboBoxServer.Items.Add("oc");
            comboBoxServer.Items.Add("pbe");
            comboBoxServer.Items.Add("tr");
        }

        private void ButtonGenerate_Click(object sender, EventArgs e)
        {
            userName = textBoxName.Text;
            server = comboBoxServer.Text;

            System.IO.StreamWriter File = new System.IO.StreamWriter("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/name.txt");
            File.Write(userName);
            File.Close();

            System.IO.StreamWriter File2 = new System.IO.StreamWriter("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/server.txt");
            File2.Write(server);
            File2.Close();

            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            cmd.StartInfo.RedirectStandardInput = true;
            cmd.StartInfo.RedirectStandardOutput = true;
            cmd.StartInfo.CreateNoWindow = true;
            cmd.StartInfo.UseShellExecute = false;
            cmd.Start();

            cmd.StandardInput.WriteLine("python {0}", @"C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/main.py");
            cmd.StandardInput.Flush();
            cmd.StandardInput.Close();
            cmd.WaitForExit();
            Console.WriteLine(cmd.StandardOutput.ReadToEnd());


        }

        private void TextBoxName_TextChanged(object sender, EventArgs e)
        {

        }

        private void ComboBoxServer_SelectedIndexChanged(object sender, EventArgs e)
        {


        }
    }
}
