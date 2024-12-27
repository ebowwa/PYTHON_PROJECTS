// Flutter web plugin registrant file.
//
// Generated file. Do not edit.
//

// @dart = 2.13
// ignore_for_file: type=lint

import 'package:audio_session/audio_session_web.dart';
import 'package:awesome_notifications/awesome_notifications_web.dart';
import 'package:awesome_notifications_core/awesome_notifications_core_web.dart';
import 'package:device_info_plus/src/device_info_plus_web.dart';
import 'package:file_picker/_internal/file_picker_web.dart';
import 'package:flutter_native_splash/flutter_native_splash_web.dart';
import 'package:flutter_sound_web/flutter_sound_web.dart';
import 'package:fonnx/fonnx_web.dart';
import 'package:mixpanel_flutter/mixpanel_flutter_web.dart';
import 'package:opus_flutter_web/opus_flutter_web.dart';
import 'package:package_info_plus/src/package_info_plus_web.dart';
import 'package:permission_handler_html/permission_handler_html.dart';
import 'package:record_web/record_web.dart';
import 'package:sensors_plus/src/sensors_plus_web.dart';
import 'package:share_plus/src/share_plus_web.dart';
import 'package:shared_preferences_web/shared_preferences_web.dart';
import 'package:url_launcher_web/url_launcher_web.dart';
import 'package:flutter_web_plugins/flutter_web_plugins.dart';

void registerPlugins([final Registrar? pluginRegistrar]) {
  final Registrar registrar = pluginRegistrar ?? webPluginRegistrar;
  AudioSessionWeb.registerWith(registrar);
  AwesomeNotificationsWeb.registerWith(registrar);
  AwesomeNotificationsCoreWeb.registerWith(registrar);
  DeviceInfoPlusWebPlugin.registerWith(registrar);
  FilePickerWeb.registerWith(registrar);
  FlutterNativeSplashWeb.registerWith(registrar);
  FlutterSoundPlugin.registerWith(registrar);
  FonnxWeb.registerWith(registrar);
  MixpanelFlutterPlugin.registerWith(registrar);
  OpusFlutterWeb.registerWith(registrar);
  PackageInfoPlusWebPlugin.registerWith(registrar);
  WebPermissionHandler.registerWith(registrar);
  RecordPluginWeb.registerWith(registrar);
  WebSensorsPlugin.registerWith(registrar);
  SharePlusWebPlugin.registerWith(registrar);
  SharedPreferencesPlugin.registerWith(registrar);
  UrlLauncherPlugin.registerWith(registrar);
  registrar.registerMessageHandler();
}
