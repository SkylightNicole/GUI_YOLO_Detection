package com.example.kokok;

import java.util.List;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface ApiService {
    @POST("phone/register")
    Call<ResponseBody> send_register(@Body Register_Json register_json);

    @POST("data")
    Call<ResponseBody> send_data(@Body RequestBody body);

    @GET("get_data")
    Call<List<ListData>> get_log();
}