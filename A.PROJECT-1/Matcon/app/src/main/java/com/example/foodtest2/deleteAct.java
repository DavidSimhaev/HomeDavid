package com.example.foodtest2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class deleteAct extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_delete);

    }
    @Override
    public void onBackPressed() {
        return;
    }
    public void startNewActivity(View v) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);

    }
}