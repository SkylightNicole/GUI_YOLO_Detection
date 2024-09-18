package com.example.banana;

import com.example.banana.Data_Sender;

import android.content.pm.PackageManager;
import android.util.Log;
import android.os.Bundle;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.content.Context;
import android.widget.Toast;
import android.widget.TextView;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
    }

    public void Send_Data(View view)
    {
        String jsonData = "{\"userId\":\"1\", \"userName\":\"John Doe\"}";
        Data_Sender Sending = new Data_Sender();
        Sending.send_data(jsonData);
        Toast.makeText(this, "Click!", Toast.LENGTH_SHORT).show();
    }
}