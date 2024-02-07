import io
import sys
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
import webbrowser
import requests
import folium
import urllib
import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

r = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1024</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1024</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Анализ климатических данных</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_7">
      <property name="spacing">
       <number>10</number>
      </property>
      <property name="sizeConstraint">
       <enum>QLayout::SetMaximumSize</enum>
      </property>
      <item>
       <widget class="QTabWidget" name="tabWidget">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
          <horstretch>1</horstretch>
          <verstretch>1</verstretch>
         </sizepolicy>
        </property>
        <property name="font">
         <font>
          <pointsize>10</pointsize>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="tabPosition">
         <enum>QTabWidget::North</enum>
        </property>
        <property name="tabShape">
         <enum>QTabWidget::Rounded</enum>
        </property>
        <property name="currentIndex">
         <number>2</number>
        </property>
        <property name="documentMode">
         <bool>true</bool>
        </property>
        <property name="tabsClosable">
         <bool>false</bool>
        </property>
        <widget class="QWidget" name="tab">
         <attribute name="title">
          <string>Навигация</string>
         </attribute>
         <layout class="QGridLayout" name="gridLayout_2" rowstretch="0">
          <item row="0" column="0">
           <layout class="QGridLayout" name="gridLayout">
            <property name="leftMargin">
             <number>5</number>
            </property>
            <property name="topMargin">
             <number>5</number>
            </property>
            <property name="rightMargin">
             <number>5</number>
            </property>
            <property name="bottomMargin">
             <number>5</number>
            </property>
            <property name="spacing">
             <number>10</number>
            </property>
            <item row="0" column="0">
             <widget class="QPushButton" name="btnDownloadTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Загрузка данных</string>
              </property>
             </widget>
            </item>
            <item row="0" column="2">
             <widget class="QPushButton" name="btnAnalizeTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Анализ данных</string>
              </property>
             </widget>
            </item>
            <item row="0" column="1">
             <widget class="QPushButton" name="btnVisualTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Визуализация данных</string>
              </property>
             </widget>
            </item>
            <item row="1" column="0">
             <widget class="QPushButton" name="btnPredictTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Прогноз</string>
              </property>
             </widget>
            </item>
            <item row="1" column="1">
             <widget class="QPushButton" name="btnMonitoringTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Мониторинг</string>
              </property>
             </widget>
            </item>
            <item row="1" column="2">
             <widget class="QPushButton" name="btnExportTab">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>200</width>
                <height>200</height>
               </size>
              </property>
              <property name="font">
               <font>
                <pointsize>12</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Экспорт</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tab_2">
         <attribute name="title">
          <string>Загрузка данных</string>
         </attribute>
         <layout class="QHBoxLayout" name="horizontalLayout_4">
          <item>
           <layout class="QVBoxLayout" name="verticalLayout_2">
            <property name="spacing">
             <number>10</number>
            </property>
            <property name="leftMargin">
             <number>10</number>
            </property>
            <property name="topMargin">
             <number>10</number>
            </property>
            <property name="rightMargin">
             <number>10</number>
            </property>
            <property name="bottomMargin">
             <number>10</number>
            </property>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout_12">
              <item>
               <widget class="QLabel" name="label_4">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                  <weight>75</weight>
                  <bold>true</bold>
                 </font>
                </property>
                <property name="text">
                 <string>Предпросмотр</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QSpinBox" name="spinBoxCountLineData">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="minimum">
                 <number>10</number>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QLabel" name="label_16">
                <property name="text">
                 <string> первых строк</string>
                </property>
               </widget>
              </item>
             </layout>
            </item>
            <item>
             <widget class="QTableWidget" name="tableWidget">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
                <horstretch>1</horstretch>
                <verstretch>1</verstretch>
               </sizepolicy>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Sunken</enum>
              </property>
              <property name="alternatingRowColors">
               <bool>false</bool>
              </property>
              <property name="selectionBehavior">
               <enum>QAbstractItemView::SelectRows</enum>
              </property>
              <attribute name="verticalHeaderStretchLastSection">
               <bool>false</bool>
              </attribute>
             </widget>
            </item>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="QPushButton" name="homeBtnDowloadTab">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>На гравную</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="downloadFileData">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>Загрузить из файла</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QLineEdit" name="lineEdit">
                <property name="text">
                 <string>Адрес</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="pushButton_7">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>Загрузить по ссылке</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="clearBtnTableWidget">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>Очистить</string>
                </property>
               </widget>
              </item>
             </layout>
            </item>
            <item>
             <widget class="QLabel" name="labelStatusDownloadData">
              <property name="frameShape">
               <enum>QFrame::Box</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <property name="lineWidth">
               <number>1</number>
              </property>
              <property name="midLineWidth">
               <number>0</number>
              </property>
              <property name="text">
               <string>Статус:</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tab_3">
         <attribute name="title">
          <string>Визуализация данных</string>
         </attribute>
         <layout class="QHBoxLayout" name="horizontalLayout_5">
          <item>
           <layout class="QGridLayout" name="gridLayout_3">
            <item row="0" column="0">
             <layout class="QVBoxLayout" name="verticalLayout_6">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="PlotWidget" name="graphicsView"/>
              </item>
              <item>
               <layout class="QGridLayout" name="gridLayout_4" columnstretch="0,0,0">
                <property name="spacing">
                 <number>10</number>
                </property>
                <item row="0" column="2">
                 <widget class="QPushButton" name="QPushButton_1">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                    <weight>75</weight>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="text">
                   <string>Местоположение</string>
                  </property>
                  <property name="margin">
                   <number>6</number>
                  </property>
                 </widget>
                </item>
                <item row="2" column="0">
                 <layout class="QVBoxLayout" name="verticalLayout_7">
                  <item>
                   <widget class="QCheckBox" name="checkBoxHumidity">
                    <property name="font">
                     <font>
                      <pointsize>10</pointsize>
                     </font>
                    </property>
                    <property name="text">
                     <string>Влажность</string>
                    </property>
                    <property name="checked">
                     <bool>false</bool>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QCheckBox" name="checkBoxPrecipitation">
                    <property name="font">
                     <font>
                      <pointsize>10</pointsize>
                     </font>
                    </property>
                    <property name="text">
                     <string>Осадки</string>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QCheckBox" name="checkBoxDirectionWind">
                    <property name="font">
                     <font>
                      <pointsize>10</pointsize>
                     </font>
                    </property>
                    <property name="text">
                     <string>Направление ветра</string>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QCheckBox" name="checkBoxTemperature">
                    <property name="font">
                     <font>
                      <pointsize>10</pointsize>
                     </font>
                    </property>
                    <property name="text">
                     <string>Температура</string>
                    </property>
                   </widget>
                  </item>
                  <item>
                   <widget class="QPushButton" name="pushBtnCheckboxesClear">
                    <property name="text">
                     <string>Сброс</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </item>
                <item row="2" column="2">
                 <widget class="QListWidget" name="listWidgetStationMeteo">
                  <property name="selectionBehavior">
                   <enum>QAbstractItemView::SelectRows</enum>
                  </property>
                  <property name="spacing">
                   <number>1</number>
                  </property>
                  <property name="sortingEnabled">
                   <bool>true</bool>
                  </property>
                 </widget>
                </item>
                <item row="6" column="2">
                 <widget class="QPushButton" name="visualizationBtn">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                   </font>
                  </property>
                  <property name="text">
                   <string>Визуализация</string>
                  </property>
                 </widget>
                </item>
                <item row="0" column="0">
                 <widget class="QLabel" name="label">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                    <weight>75</weight>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="text">
                   <string>Параметры визуализации</string>
                  </property>
                  <property name="margin">
                   <number>6</number>
                  </property>
                 </widget>
                </item>
                <item row="0" column="1">
                 <widget class="QLabel" name="label_5">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                    <weight>75</weight>
                    <bold>true</bold>
                   </font>
                  </property>
                  <property name="text">
                   <string>Временной отрезок</string>
                  </property>
                  <property name="margin">
                   <number>6</number>
                  </property>
                 </widget>
                </item>
                <item row="2" column="1">
                 <layout class="QVBoxLayout" name="verticalLayout_5">
                  <item>
                   <layout class="QHBoxLayout" name="horizontalLayout_9">
                    <item>
                     <widget class="QLabel" name="label_2">
                      <property name="font">
                       <font>
                        <pointsize>10</pointsize>
                       </font>
                      </property>
                      <property name="text">
                       <string>От</string>
                      </property>
                      <property name="alignment">
                       <set>Qt::AlignCenter</set>
                      </property>
                      <property name="margin">
                       <number>5</number>
                      </property>
                     </widget>
                    </item>
                    <item>
                     <widget class="QDateTimeEdit" name="dateTimeEdit_2">
                      <property name="font">
                       <font>
                        <pointsize>10</pointsize>
                       </font>
                      </property>
                      <property name="time">
                       <time>
                        <hour>0</hour>
                        <minute>0</minute>
                        <second>0</second>
                       </time>
                      </property>
                     </widget>
                    </item>
                    <item>
                     <widget class="QLabel" name="label_3">
                      <property name="font">
                       <font>
                        <pointsize>10</pointsize>
                       </font>
                      </property>
                      <property name="text">
                       <string>До</string>
                      </property>
                      <property name="alignment">
                       <set>Qt::AlignCenter</set>
                      </property>
                      <property name="margin">
                       <number>5</number>
                      </property>
                     </widget>
                    </item>
                    <item>
                     <widget class="QDateTimeEdit" name="dateTimeEdit">
                      <property name="font">
                       <font>
                        <pointsize>10</pointsize>
                       </font>
                      </property>
                     </widget>
                    </item>
                   </layout>
                  </item>
                  <item>
                   <layout class="QVBoxLayout" name="verticalLayout_4">
                    <item>
                     <layout class="QHBoxLayout" name="horizontalLayout_3">
                      <item>
                       <widget class="QCalendarWidget" name="calendarWidgetViz1">
                        <property name="gridVisible">
                         <bool>true</bool>
                        </property>
                       </widget>
                      </item>
                      <item>
                       <widget class="QCalendarWidget" name="calendarWidgetViz2">
                        <property name="gridVisible">
                         <bool>true</bool>
                        </property>
                       </widget>
                      </item>
                     </layout>
                    </item>
                   </layout>
                  </item>
                 </layout>
                </item>
                <item row="6" column="1">
                 <widget class="QPushButton" name="clearBtnGraphView">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                   </font>
                  </property>
                  <property name="text">
                   <string>Очистить</string>
                  </property>
                 </widget>
                </item>
                <item row="6" column="0">
                 <widget class="QPushButton" name="homeBtnVisualTab">
                  <property name="font">
                   <font>
                    <pointsize>10</pointsize>
                   </font>
                  </property>
                  <property name="text">
                   <string>На главную</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tab_4">
         <attribute name="title">
          <string>Анализ данных</string>
         </attribute>
         <layout class="QHBoxLayout" name="horizontalLayout_6">
          <item>
           <layout class="QGridLayout" name="gridLayout_5">
            <property name="spacing">
             <number>10</number>
            </property>
            <item row="3" column="1">
             <layout class="QVBoxLayout" name="verticalLayout_8">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="QTextEdit" name="textEdit"/>
              </item>
             </layout>
            </item>
            <item row="0" column="0">
             <widget class="QLabel" name="label_7">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>График 1</string>
              </property>
             </widget>
            </item>
            <item row="2" column="1">
             <widget class="QLabel" name="label_9">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>Выводы</string>
              </property>
             </widget>
            </item>
            <item row="0" column="1">
             <widget class="QLabel" name="label_8">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>График 2</string>
              </property>
             </widget>
            </item>
            <item row="1" column="1">
             <widget class="QGraphicsView" name="graphicsView_3"/>
            </item>
            <item row="1" column="0">
             <widget class="QGraphicsView" name="graphicsView_2"/>
            </item>
            <item row="3" column="0">
             <widget class="QGraphicsView" name="graphicsView_4"/>
            </item>
            <item row="2" column="0">
             <widget class="QLabel" name="label_10">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>График 3</string>
              </property>
             </widget>
            </item>
            <item row="4" column="0">
             <widget class="QPushButton" name="homeBtnAnalisTab">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
               </font>
              </property>
              <property name="text">
               <string>На главную</string>
              </property>
             </widget>
            </item>
            <item row="4" column="1">
             <widget class="QPushButton" name="pushButton_10">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
               </font>
              </property>
              <property name="text">
               <string>Экспорт</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tab_5">
         <attribute name="title">
          <string>Прогноз</string>
         </attribute>
         <layout class="QHBoxLayout" name="horizontalLayout_11">
          <property name="spacing">
           <number>10</number>
          </property>
          <property name="leftMargin">
           <number>10</number>
          </property>
          <property name="topMargin">
           <number>10</number>
          </property>
          <property name="rightMargin">
           <number>10</number>
          </property>
          <property name="bottomMargin">
           <number>10</number>
          </property>
          <item>
           <layout class="QVBoxLayout" name="verticalLayout_10">
            <property name="spacing">
             <number>10</number>
            </property>
            <item>
             <widget class="QLabel" name="label_11">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>График</string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QGraphicsView" name="graphicsView_5"/>
            </item>
            <item>
             <widget class="QPushButton" name="homeBtnPredictTab">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
               </font>
              </property>
              <property name="text">
               <string>На главную</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
          <item>
           <layout class="QVBoxLayout" name="verticalLayout_9">
            <property name="spacing">
             <number>10</number>
            </property>
            <item>
             <widget class="QLabel" name="label_12">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>Интервал</string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QCalendarWidget" name="calendarWidget_3">
              <property name="gridVisible">
               <bool>true</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QCalendarWidget" name="calendarWidget_4">
              <property name="gridVisible">
               <bool>true</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QLabel" name="label_13">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>75</weight>
                <bold>true</bold>
               </font>
              </property>
              <property name="text">
               <string>Результат</string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QTextEdit" name="textEdit_2"/>
            </item>
            <item>
             <widget class="QPushButton" name="pushButton_11">
              <property name="font">
               <font>
                <pointsize>10</pointsize>
                <weight>50</weight>
                <bold>false</bold>
               </font>
              </property>
              <property name="text">
               <string>Прогноз</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tab_6">
         <attribute name="title">
          <string>Мониторинг</string>
         </attribute>
         <layout class="QVBoxLayout" name="verticalLayout_12">
          <item>
           <layout class="QVBoxLayout" name="verticalLayout_11">
            <property name="spacing">
             <number>10</number>
            </property>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout_10">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="QLabel" name="label_14">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                  <weight>75</weight>
                  <bold>true</bold>
                 </font>
                </property>
                <property name="text">
                 <string>Текущая метеоситуация</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QLabel" name="label_15">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                  <weight>75</weight>
                  <bold>true</bold>
                 </font>
                </property>
                <property name="text">
                 <string>Источник:</string>
                </property>
               </widget>
              </item>
             </layout>
            </item>
            <item>
             <widget class="QTextBrowser" name="textBrowser"/>
            </item>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout_8">
              <property name="spacing">
               <number>10</number>
              </property>
              <item>
               <widget class="QPushButton" name="homeBtnMonitoringtab">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>На главную</string>
                </property>
               </widget>
              </item>
              <item>
               <widget class="QPushButton" name="pushButton_12">
                <property name="font">
                 <font>
                  <pointsize>10</pointsize>
                 </font>
                </property>
                <property name="text">
                 <string>Обновить</string>
                </property>
               </widget>
              </item>
             </layout>
            </item>
           </layout>
          </item>
         </layout>
        </widget>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1024</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>"""


class Monitoringiop(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(r)
        uic.loadUi(f, self)


        self.totalData = {}
        self.data = []
        self.liststations = set()
        self.sef = None
        self.flag = True
        self.time_start = []
        self.time_end = []

        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredictTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Экспорт': [self.btnExportTab.clicked.connect(self.navigate), 6]
        }

        self.downloadFileData.clicked.connect(self.loadTable)
        self.clearBtnTableWidget.clicked.connect(self.clearTableWidget)
        self.downloadFileData.clicked.connect(self.download)

        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

        self.QPushButton_1.clicked.connect(self.ip_a)
        self.pushBtnCheckboxesClear.clicked.connect(self.clear_button)

        self.visualizationBtn.clicked.connect(self.get_time)
        self.visualizationBtn.clicked.connect(self.visualization)



    # Загрузка
    def download(self):
        if '.sqlite' in self.lineEdit.text():
           print(1)
        else:
            print(0)


    # Получение временного отрезка
    def get_time(self):
        # Время начала
        self.time_start = list(map(int, str(self.dateTimeEdit_2.dateTime())[23:len(str(self.dateTimeEdit_2.dateTime())) - 1].split(", ")))
        self.time_start.reverse()
        del self.time_start[0]

        # Время конца
        self.time_end = list(map(int, str(self.dateTimeEdit.dateTime())[23:len(str(self.dateTimeEdit.dateTime())) - 1].split(", ")))
        self.time_end.reverse()
        del self.time_end[0]

        print(self.time_start)
        print(self.time_end)


    # Визуализация
    def visualization(self):
        self.graphicsView.clear()
        querry = ((self.time_end[3] - self.time_start[3]) * 365 + (self.time_end[2] - self.time_start[2]) * 30 + (self.time_end[1] - self.time_start[1])) * 24 + (self.time_end[0] - self.time_start[0])
        querries = 0
        for i in range(0, querry + 1, 3):
            querries += 1

        if self.checkBoxHumidity.isChecked():
            cursor.execute(f"SELECT humidity FROM stations")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"g"})

        if self.checkBoxPrecipitation.isChecked():
            cursor.execute(f"SELECT precipit FROM stations")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"b"})

        if self.checkBoxDirectionWind.isChecked():
            cursor.execute(f"SELECT dirwind FROM stations")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t)

        if self.checkBoxTemperature.isChecked():
            cursor.execute(f"SELECT temperature FROM stations")

            y_t = [x[0] for x in cursor.fetchmany(querries)]
            x_t = [i for i in range(querries)]

            self.graphicsView.plot(x_t, y_t, pen={"color":"r"})


    # Очистка чекбоксов
    def clear_button(self):
        self.checkBoxHumidity.setChecked(False)
        self.checkBoxPrecipitation.setChecked(False)
        self.checkBoxDirectionWind.setChecked(False)
        self.checkBoxTemperature.setChecked(False)


    # Навигация
    def navigate(self):
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])


    # На главную
    def homeGo(self):
        self.tabWidget.setCurrentIndex(0)


    def clearTableWidget(self):
        try:
            self.tableWiget.clear()
            self.data = []
        except AttributeError as e:
            print('тут ошибка', e)

    def loadTable(self):
        pass


    # Местоположение
    def ip_a(self):
        def get_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response["ip"]

        def get_location():
            ip_address = get_ip()
            location_data = {
                "ip": ip_address}
            n = ''.join([j for i, j in location_data.items()])
            return n

        def main_1():
            try:
                 url = requests.get('https://api64.ipify.org?format=json')
                 if url:
                     ip = get_location()
                     n = []
                     response = requests.get(f'http://ip-api.com/json/{ip}').json()
                     for i, j in response.items():
                         if i == 'lat' or i == 'lon':
                             n.append(j)
                     m = folium.Map(location=[n[0], n[1]], zoom_start=15)
                     folium.Marker([n[0], n[1]], poput='Место 1', tooltip=None).add_to(m)
                     m.save('weather.html')
                     webbrowser.open('weather.html')


            except requests.ConnectionError as e:
                print(e)


        if __name__ == '__main__':
            main_1()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monitoringiop()
    ex.show()
    sys.exit(app.exec_())

    # https://coderslegacy.com/python/pyqt-qcheckbox/