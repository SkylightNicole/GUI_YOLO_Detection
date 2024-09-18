package com.example.banana;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Retrofit_Instance {
    private static final String Base_Url = "https://9ceb-2001-fb1-2a-7eeb-d5be-40d7-d8dd-694f.ngrok-free.app/";
    private static Retrofit retrofit = null;
    public static ApiService getApiService()
    {
        if (retrofit==null)
        {
            retrofit = new Retrofit.Builder()
                    .baseUrl(Base_Url)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit.create(ApiService.class);
    }
}
