package com.example.banana;

import android.util.Log;

import okhttp3.MediaType;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Data_Sender{
    public void send_data(String jsonData){
        Log.d("Data_Sender","Function called!");
        ApiService apiService = Retrofit_Instance.getApiService();

        RequestBody requestBody = RequestBody.create(MediaType.parse("application/json"),jsonData);

        Call<ResponseBody> call = apiService.send_data(requestBody);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful())
                {
                    try
                    {
                        Log.d("Data_Sender","Response: " + response.body().string());
                    }
                    catch (Exception e)
                    {
                        e.printStackTrace();
                    }
                }
                else
                {
                    Log.d("Data_Sender","Request Failed with code : " + response.code());
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable throwable) {
                throwable.printStackTrace();
            }
        });
    }
}
