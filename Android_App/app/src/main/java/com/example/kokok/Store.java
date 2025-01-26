package com.example.kokok;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.content.Intent;
import android.widget.Button;
import android.widget.TextView;
import android.view.View;

public class Store extends AppCompatActivity {

    private int KhaPow = 0;
    private int Kaopad = 0;
    private int Kaijeow = 0;
    private int Sushi = 0;
    private int PadThai = 0;
    private int Tomyum = 0;

    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_store);

        textView = findViewById(R.id.ResultText);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
    /**
     * Navigator bar function
     */
    public void navi(View view)
    {
        share_function sharefunction = new share_function();
        sharefunction.navigator(this, view);
    }
    public static class vare
    {
        public static int result = 0;
    }
    public void price(View view)
    {
        if (view.getId() == R.id.khapow)
        {
            vare.result += 45;
            KhaPow += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
        else if (view.getId() == R.id.kaijeow)
        {
            vare.result += 40;
            Kaijeow += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
        else if (view.getId() == R.id.padthai)
        {
            vare.result += 45;
            PadThai += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
        else if (view.getId() == R.id.kaopad)
        {
            vare.result += 30;
            Kaopad += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
        else if (view.getId() == R.id.Sushi)
        {
            vare.result += 70;
            Sushi += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
        else if (view.getId() == R.id.Tomyum)
        {
            vare.result += 65;
            Tomyum += 1;
            textView.setText("Total : " + vare.result + "บาท");
        }
    }
    public void order(View view)
    {
        send();
        vare.result = 0;
        PopUp.showpopup(this,"Success!","Order has been placed");
    }
    public void send()
    {
        StringBuilder sb = new StringBuilder("Summary : ");
        sb.append(String.valueOf(vare.result)).append("\n");
        if (KhaPow > 0)
        {
            sb.append("Khapow : ").append(KhaPow).append("\n");
        }
        if (Kaijeow > 0)
        {
            sb.append("Kaijeow : ").append(Kaijeow).append("\n");
        }
        if (PadThai > 0)
        {
            sb.append("PadThai : ").append(PadThai).append("\n");
        }
        if (Kaopad > 0)
        {
            sb.append("KaoPad : ").append(Kaopad).append("\n");
        }
        if (Sushi > 0)
        {
            sb.append("Sushi : ").append(Sushi).append("\n");
        }
        if (Tomyum > 0)
        {
            sb.append("Tomyum : ").append(Tomyum).append("\n");
        }
        String data = sb.toString();
        Data_Sender Client = new Data_Sender();
        Client.send_data(data);
        KhaPow = 0;
        Kaijeow = 0;
        PadThai = 0;
        Kaopad = 0;
        Sushi = 0;
        Tomyum = 0;
    }

}