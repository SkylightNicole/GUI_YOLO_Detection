package com.example.kokok;

import android.os.Bundle;
import android.widget.EditText;

import android.content.Intent;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.view.View;

import java.security.NoSuchAlgorithmException;

public class Register extends AppCompatActivity {

    EditText emailtext,passwordtext,repasswordtext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        emailtext = findViewById(R.id.Reg_email);
        passwordtext = findViewById(R.id.Reg_Password);
        repasswordtext = findViewById(R.id.Re_Reg_Password);

        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_register);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
    public void register(View view)
    {
        String email = emailtext.getText().toString();
        String password = passwordtext.getText().toString();
        String check_password = repasswordtext.getText().toString();
        byte[] salt;

        if (password.equals(check_password))
        {
            try
            {
                salt = PasswordManager.getSalt();
                Register_Sender sender = new Register_Sender();
                password = PasswordManager.hashpassword(password,salt);
                sender.send_register(email, password , PasswordManager.bytesToHex(salt));
            }
            catch (NoSuchAlgorithmException e)
            {
             e.printStackTrace();
             PopUp.showpopup(this, "Error!", "There was a problem hashing the password.");
            }
        }
        else
        {
            PopUp.showpopup(this,"Error!","Passwords don't match!");
        }
    }
    public void back_to_login(View view)
    {
        Intent back_log = new Intent(this, Login.class);
        startActivity(back_log);
        finish();
    }
}