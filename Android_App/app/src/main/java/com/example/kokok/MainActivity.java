package com.example.kokok;

import android.content.Intent;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {
    private boolean isButton5Clicked = false;
    private boolean isButton7Clicked = false;
    private boolean isButton8Clicked = false;
    private boolean isButton9Clicked = false;
    private boolean isButton10Clicked = false;
    private boolean isButton11Clicked = false;

    private int KhaPhow = 0;
    private int PadPhak = 0;
    private int KaiChew = 0;
    private int KaoPad = 0;
    private int PadThai = 0;
    private int NorMai = 0;

    private TextView resultTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button5 = findViewById(R.id.button);
        Button button7 = findViewById(R.id.button2);
        Button button8 = findViewById(R.id.button3);
        Button button9 = findViewById(R.id.button4);
        Button button10 = findViewById(R.id.button5);
        Button button11 = findViewById(R.id.button6);
        resultTextView = findViewById(R.id.textView);

        button5.setOnClickListener(v -> {
            isButton5Clicked = true;
            calculateResult();
        });
        button7.setOnClickListener(v -> {
            isButton7Clicked = true;
            calculateResult();
        });
        button8.setOnClickListener(v -> {
            isButton8Clicked = true;
            calculateResult();
        });
        button9.setOnClickListener(v -> {
            isButton9Clicked = true;
            calculateResult();
        });
        button10.setOnClickListener(v -> {
            isButton10Clicked = true;
            calculateResult();
        });
        button11.setOnClickListener(v -> {
            isButton11Clicked = true;
            calculateResult();
        });

        // Assuming you want to set the click listener for a button to call disable15
        Button button = findViewById(R.id.button7); // Replace with the actual ID of the button
        button.setOnClickListener(this::disable7);
    }
    public static class var{
        public static int result = 0;
    }
    public void disable7(View v) {
        Button button = (Button) v;
        button.setText("next"); /* เปลี่ยนข้อความของปุ่ม */
        send();
        var.result = 0;
        Intent i = new Intent(this, next.class); // Replace 'NextActivity' with the actual class name
        startActivity(i);
    }
    public void send(){
        StringBuilder sb = new StringBuilder("Summary : ");
        sb.append(String.valueOf(var.result)).append("\n");
        if (KhaPhow > 0)
        {
            sb.append("KhaPhow : ").append(KhaPhow).append("\n");
        }
        if (PadPhak > 0)
        {
            sb.append("PadPhak : ").append(PadPhak).append("\n");
        }
        if (KaiChew > 0)
        {
            sb.append("Kai_Chew : ").append(KaiChew).append("\n");
        }
        if (KaoPad > 0)
        {
            sb.append("KaoPad : ").append(KaoPad).append("\n");
        }
        if (PadThai > 0)
        {
            sb.append("PadThai : ").append(PadThai).append("\n");
        }
        if (NorMai > 0)
        {
            sb.append("NorMai : ").append(NorMai).append("\n");
        }
        String data = sb.toString();
        KhaPhow = 0;
        PadPhak = 0;
        KaiChew = 0;
        KaoPad = 0;
        PadThai = 0;
        NorMai = 0;
    }

    private void calculateResult() {
        if (isButton5Clicked) {
            var.result += 35;
            KhaPhow = KhaPhow + 1;
            isButton5Clicked = false;
            //กะเพรา
        }
        if (isButton7Clicked) {
            var.result += 30;
            PadPhak = PadPhak + 1;
            isButton7Clicked = false;
            //ผัดผัก
        }
        if (isButton8Clicked) {
            var.result += 30;
            KaiChew = KaiChew + 1;
            isButton8Clicked = false;
            //ข้าวไข่เจียว
        }
        if (isButton9Clicked) {
            var.result += 40;
            KaoPad = KaoPad + 1;
            isButton9Clicked = false;
            //ข้าวผัด
        }
        if (isButton10Clicked) {
            var.result += 45;
            PadThai = PadThai + 1;
            isButton10Clicked = false;
            //ผัดไทย
        }
        if (isButton11Clicked) {
            var.result += 35;
            NorMai = NorMai + 1;
            isButton11Clicked = false;
            //หน่อไม้
        }

        resultTextView.setText("total: " + var.result + " บาท");
    }
}