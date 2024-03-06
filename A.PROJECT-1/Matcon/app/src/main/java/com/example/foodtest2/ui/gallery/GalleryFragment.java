
package com.example.foodtest2.ui.gallery;
import android.Manifest;
import android.app.AlertDialog;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.Path;
import android.graphics.PorterDuff;
import android.graphics.drawable.AnimationDrawable;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Base64;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewTreeObserver;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.foodtest2.DBHelper;

import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.example.foodtest2.DetailObjectActivity;
import com.example.foodtest2.ListActivity;
import com.example.foodtest2.R;
import com.example.foodtest2.databinding.FragmentGalleryBinding;
import com.example.foodtest2.deleteAct;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

import android.content.ContentResolver;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import android.content.res.Configuration;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import android.graphics.drawable.ShapeDrawable;
import android.graphics.drawable.shapes.Shape;


public class GalleryFragment extends Fragment {
    private FragmentGalleryBinding binding;

    boolean Check_light;
    private LinearLayout savedRootLayout;
    DBHelper dbHelper;
    private static final int PERMISSION_REQUEST_CODE = 100;
    private byte[] getBitmapAsByteArray(Bitmap bitmap) {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.PNG, 0, outputStream);
        return outputStream.toByteArray();
    }
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
    public static Bitmap decodeByteArrayToBitmap(byte[] byteArray) {
        return BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
    }
    private void increaaseTextPadding(TextView textView, int padding) {
        textView.setPadding(15, 0, padding, 0);
    };
    private void increaaseTextSize(TextView textView, float factor) {
        float currentTextSize = textView.getTextSize();


        float newTextSize = currentTextSize + factor;
        textView.setTextSize(20);
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if (requestCode == PERMISSION_REQUEST_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // Разрешение получено, выполните нужные действия
                // Здесь можно открыть изображение по URI
            } else {
                // Разрешение не предоставлено, выполните действия в случае отказа пользователя
                Toast.makeText(requireContext(), "Permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }
    private LinearLayout Process_page(Boolean booleanbundle , ContentValues contentValues, LinearLayout linearLayout ){
        SQLiteDatabase database = null;
        database = dbHelper.getReadableDatabase();

        if (booleanbundle) {
            database = dbHelper.getWritableDatabase();
            database.insert(DBHelper.TABLE_CONST, null, contentValues);}


// Создание объекта File на основе пути к файлу

// Извлечение изображения из файла


        Cursor cursor = database.query(DBHelper.TABLE_CONST, null, null,null,null,null,null, null);
        LinearLayout rootLayout = null;
        String fileName = "image_data";
        int nightModeFlags = getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK;
        Check_light = false;
        if (nightModeFlags == Configuration.UI_MODE_NIGHT_YES) {
            GradientDrawable gradientDrawable = new GradientDrawable();
            gradientDrawable.setColor(getResources().getColor(R.color.gray)); // Устанавливаем цвет фона
            gradientDrawable.setCornerRadius(10); // Устанавливаем радиус скругления углов

            // Получаем представление, к которому хотим применить фон
            // Устанавливаем созданный фоновый Drawable
            linearLayout.setBackground(gradientDrawable);
            Check_light = true;

        }
        if (cursor.moveToFirst()){
            do {
                rootLayout = new LinearLayout(requireContext());
                LinearLayout linearLayout2 = new LinearLayout(requireContext());

                int idIndex = cursor.getColumnIndex(DBHelper.KEY_ID);
                int nameIndex = cursor.getColumnIndex(DBHelper.KEY_NAME);
                int detailIndex = cursor.getColumnIndex(DBHelper.KEY_DETAIL);

                String imagePathFromDatabase = cursor.getString(cursor.getColumnIndex(DBHelper.KEY_MAIL));
                File imageFileFromDatabase = new File(imagePathFromDatabase);
                Bitmap loadedBitmap = BitmapFactory.decodeFile(imageFileFromDatabase.getAbsolutePath());





                rootLayout.setLayoutParams(new LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.MATCH_PARENT
                ));


                rootLayout.setOrientation(LinearLayout.HORIZONTAL);

                TextView textViewDetail = new TextView(requireContext());

                String ValDetail = cursor.getString(detailIndex);
                String StrID = cursor.getString(idIndex);

                textViewDetail.setText(ValDetail);
                ImageView imageView = new ImageView(requireContext());
                // Установка параметров ширины и высоты
                imageView.setLayoutParams(new ViewGroup.LayoutParams(
                        (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, 95, getResources().getDisplayMetrics()),
                        150));


                // Установка масштабирования изображения
                imageView.setScaleType(ImageView.ScaleType.CENTER_CROP);
                imageView.setPadding(30,0,0,0);

                // Создание TextView 2
                TextView textView2 = new TextView(getActivity());





                textView2.setTextColor(Color.BLACK);
                increaaseTextPadding(textView2,0);
                increaaseTextSize(textView2,1);
                textView2.setLayoutParams(new ViewGroup.LayoutParams(
                        100,
                        LinearLayout.LayoutParams.MATCH_PARENT
                ));

                // Создание TextView 3
                Button Button1 = new Button(getActivity());
                Button1.setTextSize(12);
                Button1.setText("שינוי");
                Button1.setLayoutParams(new LinearLayout.LayoutParams(160,150));
                Button1.setTextColor(Color.WHITE);
                Button1.getBackground().setColorFilter(0xFF4B42CD, PorterDuff.Mode.MULTIPLY);
                Button Button2 = new Button(getActivity());
                Button2.setTextSize(12);
                Button2.setText("מחיקה");
                Button2.setLayoutParams(new LinearLayout.LayoutParams(160,150));
                Button2.setTextColor(Color.WHITE);
                Button2.getBackground().setColorFilter( 0xFFC53C3C, PorterDuff.Mode.MULTIPLY);
                Uri UriImg = bitmapToUri(requireContext(),loadedBitmap);
                imageView.setImageURI(UriImg);
                String nameVal = cursor.getString(nameIndex);
                textView2.setText(nameVal);
                textView2.setTextDirection(View.TEXT_DIRECTION_LTR);
                if (Check_light == true) {
                    textView2.setTextColor(Color.WHITE);

                }



                if (booleanbundle) {
                    break;
                }
                linearLayout2.addView(imageView);
                linearLayout2.addView(textView2);
                rootLayout.addView(linearLayout2);
                rootLayout.addView(Button1);

                Button1.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        Intent intent = new Intent(requireContext(), DetailObjectActivity.class);
                        intent.putExtra("id", StrID);
                        intent.putExtra("name", nameVal);
                        intent.putExtra("image", imagePathFromDatabase);
                        intent.putExtra("detail", ValDetail);
                        startActivity(intent);
                    }
                });
                Button2.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        AlertDialog.Builder builder = new AlertDialog.Builder(requireContext());
                        builder.setTitle("תהליך ההסרה.");
                        builder.setMessage("האם אתה באמת רוצה למחוק את הרשומה?");
                        builder.setPositiveButton("כן", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                DBHelper dbHelper = new DBHelper(requireContext());
                                SQLiteDatabase database = dbHelper.getWritableDatabase();
                                String selecteion = "_id = ?";
                                String[] selectionArgs = {String.valueOf(StrID)};
                                int deletedRows = database.delete(DBHelper.TABLE_CONST, selecteion, selectionArgs);
                                database.close();
                                dialog.dismiss();
                                Intent intent = new Intent(requireContext(), deleteAct.class);
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
                rootLayout.addView(Button2);
                rootLayout.setPadding(0,15,0,30);


                linearLayout2.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        Intent intent = new Intent(requireContext(), DetailObjectActivity.class);
                        intent.putExtra("id", StrID);
                        intent.putExtra("name", nameVal);
                        intent.putExtra("image", imagePathFromDatabase);
                        intent.putExtra("detail", ValDetail);
                        startActivity(intent);
                    }
                });

                final LinearLayout finalRootLayout = rootLayout;
                linearLayout.addView(finalRootLayout);

                finalRootLayout.getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {
                    @Override
                    public void onGlobalLayout() {
                        // Получение родительского элемента после измерения и отображения rootLayout
                        ViewGroup parentView = (ViewGroup) textView2.getParent();
                        if (parentView != null) {
                            int parentWidthTest = parentView.getWidth();
                            // Делайте что-то с полученной шириной...
                            int parentWidth = parentWidthTest; // ширина родительского контейнера
                            int desiredWidthInPercentage = 60; // желаемая ширина textView2 в процентах

                            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(parentWidthTest, LinearLayout.LayoutParams.MATCH_PARENT, 60);
                            textView2.setLayoutParams(params);

                        } else {
                            // Обработка случая, когда родительский элемент не найден
                        }
                        // Удаление слушателя, чтобы избежать многократного вызова
                        finalRootLayout.getViewTreeObserver().removeOnGlobalLayoutListener(this);
                    }
                });



                ViewGroup parentView = (ViewGroup) textView2.getParent();
                int parentWidthTest = parentView.getWidth();
            } while (cursor.moveToNext());
        } else {
            Toast.makeText(getActivity(), "יש תקלה קטנה תנסו מאוחר יותר",Toast.LENGTH_SHORT).show();

            TextView txtEmpty = new TextView(getActivity());
            txtEmpty.setLayoutParams(new ViewGroup.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.MATCH_PARENT));
            txtEmpty.setText("הרשימה ריקה");
            txtEmpty.setGravity(Gravity.CENTER);

            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT, // Ширина равна ширине родительского контейнера
                    LinearLayout.LayoutParams.MATCH_PARENT  // Высота равна высоте родительского контейнера
            );
            layoutParams.gravity = Gravity.CENTER; // Центрируем элемент внутри родительского контейнера
            txtEmpty.setLayoutParams(layoutParams); // Устанавливаем параметры размещения для TextView
            txtEmpty.setTextSize(24);
            linearLayout.addView(txtEmpty);



        }
        cursor.close();

        return rootLayout;
    }
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        GalleryViewModel galleryViewModel =
                new ViewModelProvider(this).get(GalleryViewModel.class);
        binding = FragmentGalleryBinding.inflate(inflater, container, false);
        View root = binding.getRoot();
        dbHelper = new DBHelper(requireContext());
        Bundle bundle = getArguments();
        LinearLayout linearLayout = root.findViewById(R.id.fragment_container_Test);
// Проверяем текущую тему




        ContentValues contentValues = new ContentValues();
        if (bundle != null ) {
            String IndexStr = bundle.getString("Index");
            String resField1 = bundle.getString("field1");
            String resField2 = bundle.getString("field2");
            String UriImgStr = bundle.getString("uriImage");

            Uri imageUri = Uri.parse(UriImgStr);


            Bitmap bitmap = decodeUriToBitmap(requireContext(), imageUri);
            File imageFile = saveBitmapToFile(requireContext(), bitmap);
            String imagePath = imageFile.getAbsolutePath();


            contentValues.put(DBHelper.KEY_ID, IndexStr);
            contentValues.put(DBHelper.KEY_NAME, resField1);
            contentValues.put(DBHelper.KEY_MAIL, imagePath);
            contentValues.put(DBHelper.KEY_DETAIL, resField2);

            Process_page(true, contentValues, linearLayout);
        }
        else {Process_page(false, contentValues, linearLayout);
        }
        return root;
    }
    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}


