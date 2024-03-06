package com.example.foodtest2.ui.slideshow;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.Navigation;

import com.example.foodtest2.ListActivity;
import com.example.foodtest2.MainActivity;
import com.example.foodtest2.R;
import com.example.foodtest2.databinding.FragmentSlideshowBinding;
import com.example.foodtest2.ui.gallery.GalleryFragment;
import com.google.android.material.textfield.TextInputEditText;
import com.example.foodtest2.databinding.FragmentGalleryBinding;

import java.io.File;


public class SlideshowFragment extends Fragment {
    private static final int REQUEST_CODE_PERMISSION = 123;

    private FragmentSlideshowBinding binding;
    private TextInputEditText field1;
    private String UriImage;
    private TextInputEditText field2;
    private static final int PICK_FILE_REQUEST_CODE = 1;
    private boolean isHebrew(String text) {
        // Создаем регулярное выражение для проверки, содержит ли текст иврит
        String hebrewPattern = ".*[\\u0590-\\u05FF].*"; // Диапазон символов иврита в Unicode

        // Проверяем, соответствует ли текст регулярному выражению
        return text.matches(hebrewPattern);
    }
    // Метод для проверки, начинается ли строка с иврита
    private boolean startsWithHebrew(char c) {
        // Проверяем, начинается ли символ с символов иврита в Unicode
        return c >= '\u0590' && c <= '\u05FF';
    }

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        SlideshowViewModel slideshowViewModel =
                new ViewModelProvider(this).get(SlideshowViewModel.class);
        binding = FragmentSlideshowBinding.inflate(inflater, container, false);
        View root = binding.getRoot();
        Button btn_img = root.findViewById(R.id.button17);




        btn_img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                pickFile();

            }
        });

        field1 = root.findViewById(R.id.fieldName_1);

        field1.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                // Ничего не делаем перед изменением текста
            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                // Проверяем, является ли введенная первая буква ивритом
                if (s.length() > 0 && !startsWithHebrew(s.charAt(0))) {
                    // Если первая буква не является ивритом, устанавливаем сообщение об ошибке в TextInputLayout
                    field1.setError("אנא הזן את הטקסט בעברית בלבד");
                } else {
                    // Если первая буква является ивритом, убираем сообщение об ошибке в TextInputLayout
                    field1.setError(null);
                }
            }
            @Override
            public void afterTextChanged(Editable s) {
                // Ничего не делаем после изменения текста
            }
        });
        field2 = root.findViewById(R.id.fieldName_2);
        field2.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                // Ничего не делаем перед изменением текста
            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                // Проверяем, является ли введенная первая буква ивритом
                if (s.length() > 0 && !startsWithHebrew(s.charAt(0))) {
                    // Если первая буква не является ивритом, устанавливаем сообщение об ошибке в TextInputLayout
                    field2.setError("אנא הזן את הטקסט בעברית בלבד");
                } else {
                    // Если первая буква является ивритом, убираем сообщение об ошибке в TextInputLayout
                    field2.setError(null);
                }
            }
            @Override
            public void afterTextChanged(Editable s) {
                // Ничего не делаем после изменения текста
            }
        });



        Button my_button = root.findViewById(R.id.my_button);

        my_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String resField1 = field1.getText().toString(); /*СТРОКА ПЕРВОГО ПОЛЯ*/
                String resField2 = field2.getText().toString(); /*СТРОКА ВТОРОГО ПОЛЯ*/
                String UriImg = UriImage; /*ССЫЛКА НА КАРТИНКУ*/
                Bundle bundle = new Bundle();
                bundle.putString("field1", resField1);
                bundle.putString("field2", resField2);
                bundle.putString("uriImage", UriImg);

                CharSequence error = field1.getError();
                if (error != null && error.length() > 0) {
                    Toast.makeText(getActivity(), "אנא הזן את הטקסט בעברית בלבד", Toast.LENGTH_SHORT).show();
                    return;
                }
                CharSequence error2 = field2.getError();
                if (error2 != null && error2.length() > 0) {
                    Toast.makeText(getActivity(), "אנא הזן את הטקסט בעברית בלבד", Toast.LENGTH_SHORT).show();
                    return;
                }


                if (!resField1.isEmpty() && !resField2.isEmpty() && UriImg != null )  {
                    // Создаем Bundle для передачи данных
                    Navigation.findNavController(v).navigate(R.id.nav_gallery, bundle);
                    Intent intent = new Intent(requireContext(), ListActivity.class);
                    startActivity(intent);

                } else {
                    // Показываем сообщение пользователю о необходимости заполнения всех полей
                    Toast.makeText(getActivity(), "בבקשה מלא את כל השדות", Toast.LENGTH_SHORT).show();
                }
            }
        });



        return root;
    }
    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }


    private void pickFile() {
        // Создаем Intent для выбора файла
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("image/*"); // Указываем тип файлов, которые можно выбирать
        intent.addCategory(Intent.CATEGORY_OPENABLE);

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
                Toast.makeText(requireContext(), "Permission denied", Toast.LENGTH_SHORT).show(); }
        }};


    @Override
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        // Проверяем, что получили ответ из диалогового окна выбора файла и успешно выбрали файл
        if (requestCode == PICK_FILE_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            if (data != null && data.getData() != null) {
                // Получаем Uri выбранного файла
                Uri fileUri = data.getData();
                // Теперь можно работать с выбранным файлом, например, получить его путь или открыть его поток для чтения
                // Для примера, можно вывести путь выбранного файла в лог
                /*String resStrUser = fileOriginalUser.substring(Math.max(fileOriginalUser.length()-10,0)); 10 - СИМВОЛЬНОЕ ИМЯ КАРТИНКИ ЕСЛИ КОГДА НИБУДЬ ПОТРЕБУЕТСЯ*/
                Toast.makeText(getActivity(), "התמונה הועלתה בהצלחה",Toast.LENGTH_SHORT).show();


                UriImage = fileUri.toString();


            }
        }
    }
    private String getRealPathFromURI(Uri contentURI) {
        String result;
        Cursor cursor = getContext().getContentResolver().query(contentURI, null, null, null, null);
        if (cursor == null) { // Source is Dropbox or other similar local file path
            result = "content:/" + contentURI.getPath();
        } else {
            cursor.moveToFirst();
            int idx = cursor.getColumnIndex(MediaStore.Images.ImageColumns.DATA);
            result = cursor.getString(idx);
            cursor.close();
        }
        return result;
    }
}
