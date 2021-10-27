package com.example.deeplinkhijackingpoc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class DeepLinkHijackActivity extends AppCompatActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button resetButton = findViewById(R.id.resetButton);
        resetButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                DeepLinkHijackActivity.this.reset(view);
            }
        });

        displayHijackedLink();
    }

    public void displayHijackedLink()
    {
        // Get the Intent that started this activity and extract the URI
        Intent intent = getIntent();
        Uri uri = intent.getData();

        if(uri != null)
        {
            // Capture the layout's TextView and set the string as the URI
            TextView textView = findViewById(R.id.textView);
            textView.setText(uri.toString());
        }
    }

    @Override
    protected void onNewIntent(Intent intent)
    {
        super.onNewIntent(intent);
        this.displayHijackedLink();
    }

    public void reset(View view)
    {
        TextView textView = findViewById(R.id.textView);
        textView.setText("No Deep Link Hijacked");
    }
}