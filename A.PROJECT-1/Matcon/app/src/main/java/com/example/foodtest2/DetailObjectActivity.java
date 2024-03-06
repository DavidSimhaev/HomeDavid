package com.example.foodtest2;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.content.FileProvider;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.example.foodtest2.DBHelper;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.Configuration;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.PorterDuff;
import android.graphics.Rect;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewTreeObserver;
import android.view.Window;
import android.view.WindowId;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.foodtest2.ui.gallery.GalleryFragment;
import com.google.android.gms.pay.Pay;
import com.google.android.gms.pay.PayApiAvailabilityStatus;
import com.google.android.gms.pay.PayClient;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.UUID;
import com.example.foodtest2.databinding.ActivityDetailObjectBinding;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.textfield.TextInputEditText;
import com.squareup.picasso.BuildConfig;

import org.w3c.dom.Text;
public class DetailObjectActivity extends AppCompatActivity {
    private static final int ADD_TO_WALLET_REQUEST_CODE = 1000;
    DBHelper dbHelper;

    String UriImage;

    private static final int REQUEST_CODE_PERMISSION = 123;

    private static String req_ID;

    private static final int PICK_FILE_REQUEST_CODE = 1;

    private ActivityDetailObjectBinding layout;
    private PayClient walletClient;

    private boolean first;
    public static Bitmap decodeByteArrayToBitmap(byte[] byteArray) {
        return BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
    }
    private static File saveBitmapToFile(Context context, Bitmap bitmap) {
        String fileName = "image_" + System.currentTimeMillis() + ".jpg";
        File file = new File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), fileName);
        try {
            FileOutputStream fos = new FileOutputStream(file);
            bitmap.compress(Bitmap.CompressFormat.JPEG, 100, fos);
            fos.flush();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return file;
    }
    public static Uri bitmapToUri(Context context, Bitmap bitmap) {
        File file = saveBitmapToFile(context, bitmap);
        return Uri.fromFile(file);
    }
    private View addToWalletButton;

    public static Bitmap decodeUriToBitmap(Context context, Uri uri) {
        Bitmap bitmap = null;
        try {
            ContentResolver contentResolver = context.getContentResolver();
            InputStream inputStream = contentResolver.openInputStream(uri);
            bitmap = BitmapFactory.decodeStream(inputStream);
            if (inputStream != null) {
                inputStream.close();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return bitmap;
    }
    private boolean startsWithHebrew(char c) {
        // Проверяем, начинается ли символ с символов иврита в Unicode
        return c >= '\u0590' && c <= '\u05FF';
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        walletClient = Pay.getClient(this);
        layout = ActivityDetailObjectBinding.inflate(getLayoutInflater());
        setContentView(R.layout.activity_detail_object);
        setContentView(layout.getRoot());
        ActionBar actionBar = getSupportActionBar();
        // Устанавливаем пользовательское представление для ActionBar
        actionBar.setDisplayOptions(ActionBar.DISPLAY_SHOW_CUSTOM);
        actionBar.setCustomView(R.layout.layoutuse);
        FloatingActionButton fab = findViewById(R.id.custom_button);
        FrameLayout frameLayout = findViewById(R.id.frame_detail_data);
        int nightModeFlags = getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK;
        if (nightModeFlags == Configuration.UI_MODE_NIGHT_YES) {
            GradientDrawable gradientDrawable = new GradientDrawable();
            gradientDrawable.setColor(getResources().getColor(R.color.gray)); // Устанавливаем цвет фона
            gradientDrawable.setCornerRadius(10); // Устанавливаем радиус скругления углов
            // Получаем представление, к которому хотим применить фон
            // Устанавливаем созданный фоновый Drawable
            frameLayout.setBackground(gradientDrawable);

        }

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
        Bundle extras = getIntent().getExtras();
            if (extras != null) {
                String id = extras.getString("id");
                String name = extras.getString("name");
                String image = extras.getString("image");
                String detail = extras.getString("detail");
                Button deleteDate = findViewById(R.id.button4);
                deleteDate.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        AlertDialog.Builder builder = new AlertDialog.Builder(DetailObjectActivity.this);
                        builder.setTitle("תהליך ההסרה.");
                        builder.setMessage("האם אתה באמת רוצה למחוק את הרשומה?");
                        builder.setPositiveButton("כן", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                DBHelper dbHelper = new DBHelper(DetailObjectActivity.this);
                                SQLiteDatabase database = dbHelper.getWritableDatabase();
                                String selecteion = "_id = ?";
                                String[] selectionArgs = {String.valueOf(id)};
                                int deletedRows = database.delete(DBHelper.TABLE_CONST, selecteion, selectionArgs);
                                database.close();
                                dialog.dismiss();
                                Intent intent = new Intent(DetailObjectActivity.this, deleteAct.class);
                                startActivity(intent);
                            }
                        });
                        builder.setNegativeButton("לא", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.dismiss();
                            }
                        });
                        builder.show();
                    }
                });
                File imageFileFromDatabase = new File(image);
                Bitmap loadedBitmap = BitmapFactory.decodeFile(imageFileFromDatabase.getAbsolutePath());
                Uri UriImg = bitmapToUri(this,loadedBitmap);
                ImageView imageView = this.findViewById(R.id.imageView3);
                TextView textView = this.findViewById(R.id.title);
                TextView textView2 = this.findViewById(R.id.textView5);
                textView.setText(name);
                textView.setTextDirection(View.TEXT_DIRECTION_LTR);
                imageView.setImageURI(UriImg);
                textView2.setTextDirection(View.TEXT_DIRECTION_RTL);
                textView2.setText("            " + detail);
                Button EditDate = findViewById(R.id.button5);

                first = true;
                EditDate.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        if (first == true){
                            first = false;
                        } else {
                            return;
                        }



                        ScrollView ScrollOBJ = findViewById(R.id.ScrollViewTextDet);
                        String Stringwithoutsym = textView2.getText().toString().substring(12);
                        String StringNAME = textView.getText().toString();
                        TextInputEditText textInputEditText = new TextInputEditText(DetailObjectActivity.this);
                        textInputEditText.addTextChangedListener(new TextWatcher() {
                            @Override
                            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                                // Ничего не делаем перед изменением текста
                            }
                            @Override
                            public void onTextChanged(CharSequence s, int start, int before, int count) {
                                // Проверяем, является ли введенная первая буква ивритом
                                if (s.length() > 0 && !startsWithHebrew(s.charAt(0))) {
                                    // Если первая буква не является ивритом, устанавливаем сообщение об ошибке в TextInputLayout
                                    textInputEditText.setError("אנא הזן את הטקסט בעברית בלבד");
                                } else {
                                    // Если первая буква является ивритом, убираем сообщение об ошибке в TextInputLayout
                                    textInputEditText.setError(null);
                                }
                            }
                            @Override
                            public void afterTextChanged(Editable s) {
                                // Ничего не делаем после изменения текста
                            }
                        });





                        textInputEditText.setLayoutParams(textView2.getLayoutParams());
                        textInputEditText.setText(Stringwithoutsym);
                        textInputEditText.setHint(textView2.getHint());
                        textInputEditText.setTextDirection(View.TEXT_DIRECTION_RTL);
                        ViewGroup parentView = (ViewGroup) textView2.getParent();
                        int textViewIndex = parentView.indexOfChild(textView2);
                        parentView.removeView(textView2);
                        parentView.addView(textInputEditText, textViewIndex);
                        TextInputEditText textInputEditText2 = new TextInputEditText(DetailObjectActivity.this);
                        textInputEditText2.addTextChangedListener(new TextWatcher() {
                            @Override
                            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                                // Ничего не делаем перед изменением текста
                            }
                            @Override
                            public void onTextChanged(CharSequence s, int start, int before, int count) {
                                // Проверяем, является ли введенная первая буква ивритом
                                if (s.length() > 0 && !startsWithHebrew(s.charAt(0))) {
                                    // Если первая буква не является ивритом, устанавливаем сообщение об ошибке в TextInputLayout
                                    textInputEditText2.setError("אנא הזן את הטקסט בעברית בלבד");
                                } else {
                                    // Если первая буква является ивритом, убираем сообщение об ошибке в TextInputLayout
                                    textInputEditText2.setError(null);
                                }
                            }
                            @Override
                            public void afterTextChanged(Editable s) {
                                // Ничего не делаем после изменения текста
                            }
                        });



                        textInputEditText2.setLayoutParams(textView.getLayoutParams());
                        textInputEditText2.setText(StringNAME);
                        textInputEditText2.setHint(textView.getHint());
                        ViewGroup parentView2 = (ViewGroup) textView.getParent();
                        int textViewIndex2 = parentView.indexOfChild(textView);
                        parentView2.removeView(textView);
                        parentView2.addView(textInputEditText2, textViewIndex2);
                        textInputEditText.requestFocus();
                        InputMethodManager IMM = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
                        final View rootView = getWindow().getDecorView().getRootView();
// Установка слушателя изменений видимости клавиатуры
                        rootView.getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {
                            @Override
                            public void onGlobalLayout() {
                                Rect r = new Rect();
                                rootView.getWindowVisibleDisplayFrame(r);
                                int screenHeight = rootView.getHeight();
                                int keypadHeight = screenHeight - r.bottom;
                                if (keypadHeight < screenHeight * 0.15) {
                                    // Клавиатура скрыта
                                    // Добавьте ваш код здесь для обработки этого события
                                    ScrollOBJ.setLayoutParams(new
                                            ScrollView.LayoutParams(
                                            ScrollView.LayoutParams.MATCH_PARENT,
                                            ScrollView.LayoutParams.MATCH_PARENT
                                    ));
                                } else {
                                    ScrollOBJ.setLayoutParams(new
                                            ScrollView.LayoutParams(
                                            ScrollView.LayoutParams.MATCH_PARENT,
                                            340));
                                }
                            }
                        });
                        IMM.showSoftInput(textInputEditText, InputMethodManager.SHOW_IMPLICIT);
                        LinearLayout FrameDetText = findViewById(R.id.frameDetText);
                        Button BtnChange = findViewById(R.id.button11);
                        FrameDetText.removeView(BtnChange);
                        Button newButton = new Button(DetailObjectActivity.this); // создание новой кнопки
                        newButton.setText("קבל"); // установка текста на новой кнопке
                        newButton.getBackground().setColorFilter(0xFF4B42CD, PorterDuff.Mode.MULTIPLY);
                        newButton.setTextColor(Color.WHITE);
                        newButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {

                                CharSequence error = textInputEditText.getError();
                                CharSequence error2 = textInputEditText2.getError();

                                if (error != null && error.length() > 0 && error2 != null && error2.length() > 0 ) {
                                    Toast.makeText(DetailObjectActivity.this, "אנא הזן את הטקסט בעברית בלבד", Toast.LENGTH_SHORT).show();
                                    return;
                                }
                                String ResCgangeData = textInputEditText.getText().toString();
                                String NameGhangeStr = textInputEditText2.getText().toString();


                                if (ResCgangeData.isEmpty() || NameGhangeStr.isEmpty() ){
                                    Toast.makeText(DetailObjectActivity.this, "בבקשה מלא את כל השדות", Toast.LENGTH_SHORT).show();
                                    return;
                                }

                                AlertDialog.Builder builder2 = new AlertDialog.Builder(DetailObjectActivity.this);
                                builder2.setTitle("תהליך שינוי.");
                                builder2.setMessage("האם אתה רוצה לבצע שינויים בנתונים??");
                                builder2.setPositiveButton("כן", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        ScrollView ScrollOBJ = findViewById(R.id.ScrollViewTextDet);
                                        TextView nameViewChange = new TextView(DetailObjectActivity.this);
                                        TextView textViewChange = new TextView(DetailObjectActivity.this);
                                        textView.setText(NameGhangeStr);
                                        textView2.setText(ResCgangeData);
                                        int textViewIndex = parentView.indexOfChild(textInputEditText);
                                        parentView.removeView(textInputEditText);
                                        parentView.addView(textView2, textViewIndex);
                                        int textViewIndex2 = parentView2.indexOfChild(textInputEditText2);
                                        parentView2.removeView(textInputEditText2);
                                        parentView2.addView(textView, textViewIndex);
                                        FrameDetText.removeView(newButton);
                                        FrameDetText.addView(BtnChange);

                                        DBHelper dbHelper1 = new DBHelper(DetailObjectActivity.this);
                                        SQLiteDatabase database = dbHelper1.getWritableDatabase();
                                        ContentValues values = new ContentValues();
                                        values.put("detail", ResCgangeData); // your_column_name - имя столбца, newValue - новое значение
                                        values.put("name", NameGhangeStr); // your_column_name - имя столбца, newValue - новое значение
                                        String selection = "_id = ?"; // условие для выборки по основному _id
                                        String[] selectionArgs = { String.valueOf(id) }; // значение основного _id
                                        int count = database.update(DBHelper.TABLE_CONST, values, selection, selectionArgs);
                                        dialog.dismiss();
                                        Intent intent = new Intent(DetailObjectActivity.this, getdataAct.class);
                                        startActivity(intent);
                                    }
                                });
                                builder2.setNegativeButton("לא", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        dialog.dismiss();
                                    }
                                });
                                builder2.show();
                            }
                        });
                        FrameDetText.addView(newButton);
                    }
                });
                Button BtnChangeIMG = findViewById(R.id.button6);
                BtnChangeIMG.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        AlertDialog.Builder builder = new AlertDialog.Builder(DetailObjectActivity.this);
                        builder.setTitle("תהליך ההסרה.");
                        builder.setMessage("האם אתה רוצה להחליף תמונה?");
                        builder.setPositiveButton("כן", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.dismiss();
                                req_ID = id;
                                pickFile();
                            }
                        }) ;

                        builder.setNegativeButton("לא", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.dismiss();
                            }
                        }) ;
                        builder.show();
                    }
                });

                Button BtnSend = findViewById(R.id.button11);
                // Обработчик нажатия на кнопку "Поделиться"
                BtnSend.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        // Создаем Intent с действием ACTION_SEND
                        Intent shareIntent = new Intent(Intent.ACTION_SEND);
// Устанавливаем тип контента для передачи
                        shareIntent.setType("image/*");

                        String Stringwithoutsym = textView2.getText().toString().substring(12);

                        shareIntent.putExtra(Intent.EXTRA_TEXT, textView.getText().toString() + "\n\n" + Stringwithoutsym);
// Создаем Intent для отображения диалога "Поделиться"
                        Intent chooserIntent = Intent.createChooser(shareIntent, "Поделиться с помощью");
// Проверяем, есть ли активити, способные обработать Intent
                        if (shareIntent.resolveActivity(getPackageManager()) != null) {
                            // Если есть, запускаем Intent
                            startActivity(chooserIntent);
                        } else {
                            // Если нет, выводим сообщение об ошибке
                            Toast.makeText(getApplicationContext(), "Нет приложений для передачи", Toast.LENGTH_SHORT).show();
                        }
                    }
                });


            }
    }
    private void onAddToWalletClicked() {
        final SamplePass samplePass = new SamplePass(
                "",  // TODO(you) – Enter issuer email address
                "",    // TODO(you) – Enter issuer id
                "",  // TODO(you) – Enter pass class
                UUID.randomUUID().toString()
        );

        walletClient.savePasses(
                samplePass.toJson(),
                this,
                ADD_TO_WALLET_REQUEST_CODE
        );
    }
    private void fetchCanUseGoogleWalletApi() {
        walletClient
                .getPayApiAvailabilityStatus(PayClient.RequestType.SAVE_PASSES)
                .addOnSuccessListener(result -> {
                    // Display the "Add to Wallet" button if the wallet API is available on this device.
                    if (result == PayApiAvailabilityStatus.AVAILABLE) {
                        addToWalletButton.setVisibility(View.VISIBLE);
                    } else {
                        addToWalletButton.setVisibility(View.GONE);
                    }
                })
                .addOnFailureListener(exception -> {
                    // Hide the button and optionally show an error message
                    addToWalletButton.setVisibility(View.GONE);

                    Toast.makeText(
                            this,
                            R.string.google_wallet_status_unavailable,
                            Toast.LENGTH_SHORT
                    ).show();
                });
    }

    /**
     * Handle the result from {@link PayClient#savePasses(String, Activity, int)}, where we check to
     * see if our attempt to add the pass to the user's Google Wallet was successful, or not.
     * <p>
     * It is up to the implementer to appropriately handle error cases.
     */

    private void pickFile() {
        // Создаем Intent для выбора файла
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("image/*"); // Указываем тип файлов, которые можно выбирать
        // Запускаем Intent с запросом выбора файла
        startActivityForResult(Intent.createChooser(intent, "Выберите файл"), PICK_FILE_REQUEST_CODE);

    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_CODE_PERMISSION) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // Разрешение предоставлено, выполнение операции чтения файла изображения
                pickFile();
            } else {
                // Разрешение не предоставлено, выполните необходимые действия
                Toast.makeText(DetailObjectActivity.this, "Permission denied", Toast.LENGTH_SHORT).show(); }
        }};


    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_FILE_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            if (data != null && data.getData() != null) {
                // Получаем Uri выбранного файла
                Uri fileUri = data.getData();
                // Теперь можно работать с выбранным файлом, например, получить его путь или открыть его поток для чтения
                // Для примера, можно вывести путь выбранного файла в лог
                /*String resStrUser = fileOriginalUser.substring(Math.max(fileOriginalUser.length()-10,0)); 10 - СИМВОЛЬНОЕ ИМЯ КАРТИНКИ ЕСЛИ КОГДА НИБУДЬ ПОТРЕБУЕТСЯ*/
                UriImage = fileUri.toString();
                ImageView IMG = findViewById(R.id.imageView3);
                Uri UriImg = Uri.parse(UriImage);
                IMG.setImageURI(UriImg);


                Bitmap bitmap = decodeUriToBitmap(DetailObjectActivity.this, UriImg);
                File imageFile = saveBitmapToFile(DetailObjectActivity.this, bitmap);
                String imagePath = imageFile.getAbsolutePath();




                DBHelper dbHelper2 = new DBHelper(DetailObjectActivity.this);
                SQLiteDatabase database = dbHelper2.getWritableDatabase();
                ContentValues values = new ContentValues();
                values.put("mail", imagePath); // your_column_name - имя столбца, newValue - новое значение

                String selection = "_id = ?"; // условие для выборки по основному _id
                String[] selectionArgs = { String.valueOf(req_ID) }; // значение основного _id
                int count = database.update(DBHelper.TABLE_CONST, values, selection, selectionArgs);
                Intent intent = new Intent(DetailObjectActivity.this, getdataAct.class);
                startActivity(intent);

            }
        }
        if (requestCode == ADD_TO_WALLET_REQUEST_CODE) {
            if (resultCode == RESULT_OK) {
                Toast.makeText(
                        this,
                        R.string.add_google_wallet_success,
                        Toast.LENGTH_SHORT
                ).show();
            } else if (resultCode == RESULT_CANCELED) {
                Toast.makeText(
                        this,
                        R.string.add_google_wallet_cancelled,
                        Toast.LENGTH_SHORT
                ).show();
            } else if (resultCode == PayClient.SavePassesResult.SAVE_ERROR) {
                // Handle the error message and optionally display it to the user.
                final String errorMessage = data.getStringExtra(PayClient.EXTRA_API_ERROR_MESSAGE);
                Toast.makeText(
                        this,
                        errorMessage != null
                                ? errorMessage
                                : getString(R.string.add_google_wallet_unknown_error),
                        Toast.LENGTH_SHORT
                ).show();
            } else {
                Toast.makeText(
                        this,
                        R.string.add_google_wallet_unknown_error,
                        Toast.LENGTH_SHORT
                ).show();
            }
        }
    }
}