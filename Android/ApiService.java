package com.example.banana;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiService {
    @POST("data")
    Call<ResponseBody> send_data(@Body RequestBody body);
}
