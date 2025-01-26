package com.example.kokok;

import com.google.gson.annotations.SerializedName;

public class ListData {
    private String Username;
    private String Password;
    private String Salt;

    public ListData(String username,String password,String Salt)
    {
        this.Username = username;
        this.Password = password;
        this.Salt = Salt;
    }

    public String getUsername()
    {
        return Username;
    }
    public String getPassword()
    {
        return Password;
    }
    public String getSalt()
    {
        return Salt;
    }

    public void setUsername(String User)
    {
        this.Username = User;
    }
    public void setPassword(String Pass)
    {
        this.Password = Pass;
    }
    public void setSalt(String Salt)
    {
        this.Salt = Salt;
    }
}
