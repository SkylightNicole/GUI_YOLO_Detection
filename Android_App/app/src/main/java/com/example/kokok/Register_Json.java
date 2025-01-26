package com.example.kokok;

public class Register_Json {
    private String Username;
    private String Password;
    private String Salt;

    public Register_Json(String User,String Pass,String Salt)
    {
        this.Username = User;
        this.Password = Pass;
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
