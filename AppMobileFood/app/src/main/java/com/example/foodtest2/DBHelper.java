package com.example.foodtest2;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;


public class DBHelper extends SQLiteOpenHelper {

    public static final int DATABASE_VERSION = 2;


    public static final String DATABASE_NAME = "contactDb";

    public static final String TABLE_CONST = "contacts";


    public static final String KEY_ID = "_id";

    public static final String KEY_NAME = "name";

    public static final String KEY_MAIL = "mail";

    public static final String KEY_DETAIL = "detail";

    public DBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("create table "+ TABLE_CONST + " (" + KEY_ID
                + " integer primary key," + KEY_NAME + " text," + KEY_MAIL + " text," + KEY_DETAIL + " text" + ")");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("drop table if exists "+ TABLE_CONST);

        onCreate(db);
    }
}
