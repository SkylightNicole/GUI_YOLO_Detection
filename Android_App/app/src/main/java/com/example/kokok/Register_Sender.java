package com.example.kokok;

import android.util.Log;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Register_Sender{
    public void send_register(String Username, String Password, String Salt){
        Log.d("Register","Function called!");
        ApiService apiService = Retrofit_Instance.getApiService();

        Register_Json register_json = new Register_Json(Username,Password,Salt);

        Call<ResponseBody> call = apiService.send_register(register_json);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful())
                {
                    try
                    {
                        Log.d("Register","Response: " + response.body().string());
                    }
                    catch (Exception e)
                    {
                        e.printStackTrace();
                    }
                }
                else
                {
                    Log.d("Register","Request Failed with code : " + response.code());
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable throwable) {
                throwable.printStackTrace();
            }
        });
    }
}
