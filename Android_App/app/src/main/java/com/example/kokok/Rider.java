package com.example.kokok;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.content.Intent;
import android.view.View;
import android.widget.TextView;

public class Rider extends AppCompatActivity {

    private TextView name,phone,color,plate,price;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_rider);

        name = findViewById(R.id.Name);
        phone = findViewById(R.id.phone_num);
        color = findViewById(R.id.ve_color);
        plate = findViewById(R.id.ve_plate);
        price = findViewById(R.id.Price);

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
}