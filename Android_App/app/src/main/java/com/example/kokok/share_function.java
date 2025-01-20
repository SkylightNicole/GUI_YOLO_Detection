package com.example.kokok;

import static androidx.core.content.ContextCompat.startActivity;

import android.content.Intent;
import android.content.Context;
import android.view.View;

public class share_function {
    /**
     * This is Navigator bar function that switch views depend on which picture is clicked.
     */
    public void navigator(Context activity,View view)
    {
        if (view.getId() == R.id.rider)
        {
            Intent rider = new Intent(activity,Rider.class);
            activity.startActivity(rider);
        }
        else if (view.getId() == R.id.store)
        {
            Intent store = new Intent(activity,Store.class);
            activity.startActivity(store);
        } else if (view.getId() == R.id.profile)
        {
            Intent profile = new Intent(activity, Profile.class);
            activity.startActivity(profile);
        }
        else if (view.getId() == R.id.setting)
        {
            Intent setting = new Intent(activity,Settings.class);
            activity.startActivity(setting);
        }
    }
}
