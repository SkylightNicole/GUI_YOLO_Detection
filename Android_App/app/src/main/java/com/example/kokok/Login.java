package com.example.kokok;

import android.os.Bundle;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.view.View;
import android.widget.Toast;
import android.content.Intent;

public class Login extends AppCompatActivity {

    private EditText emailtext,passwordtext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);

        emailtext = findViewById(R.id.Log_Email);
        passwordtext = findViewById(R.id.Log_Password);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
    public void login(View view)
    {
        String email = emailtext.getText().toString();
        String password = passwordtext.getText().toString();

        if (!email.isEmpty() && !password.isEmpty())
        {
            check(email,password);
        }
        else
        {
            Toast.makeText(this,"Please fill in both field",Toast.LENGTH_SHORT).show();
        }

    }

    public void check(String email,String pass)
    {
        ;
    }
}