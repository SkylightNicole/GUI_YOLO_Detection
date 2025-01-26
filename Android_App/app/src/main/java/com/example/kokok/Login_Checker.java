package com.example.kokok;

import android.util.Log;

import java.security.NoSuchAlgorithmException;
import java.util.List;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Login_Checker {
    public void get_log(String email, String pass, Data_Callback callback)
    {
        ApiService apiService = Retrofit_Instance.getApiService();

        Call<List<ListData>> call = apiService.get_log();
        call.enqueue(new Callback<List<ListData>>() {
            @Override
            public void onResponse(Call<List<ListData>> call, Response<List<ListData>> response) {
                if (response.isSuccessful() && response.body() != null)
                {
                    List<ListData> ListData = response.body();
                    boolean check = false;
                    for (ListData data : ListData)
                    {
                        byte[] Salt;
                        String check_pass = "";
                        Salt = PasswordManager.HexToBytes(data.getSalt());
                        try
                        {
                            check_pass = PasswordManager.hashpassword(pass, Salt);
                        }
                        catch (NoSuchAlgorithmException e)
                        {
                            e.printStackTrace();
                        }
                        if (data.getUsername().equals(email) && data.getPassword().equals(check_pass))
                        {
                            check = true;
                            break;
                        }
                    }
                    callback.onresult(check);
                }
                else
                {
                    Log.d("Data_Sender", "Request failed with code : " + response.body());
                }
            }
            @Override
            public void onFailure(Call<List<ListData>> call, Throwable throwable) {
                throwable.printStackTrace();
            }
        });
    }
}
