import React from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet } from 'react-native';

const FlashDealStarHome = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>My FlashDeal Star</Text>

      {/* النجمة المركزية */}
      <Image source={require('./assets/star.png')} style={styles.star} />

      {/* الرموز الأربعة */}
      <View style={styles.iconRow}>
        <Image source={require('./assets/fingerprint.png')} style={styles.icon} />
        <Image source={require('./assets/face.png')} style={styles.icon} />
      </View>
      <View style={styles.iconRow}>
        <Image source={require('./assets/gesture.png')} style={styles.icon} />
        <Image source={require('./assets/keypad.png')} style={styles.icon} />
      </View>

      {/* شريط اختيار اللغة */}
      <View style={styles.languageBar}>
        <TouchableOpacity style={styles.langButton}>
          <Image source={require('./assets/uk.png')} style={styles.flag} />
          <Text style={styles.langText}>English</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.langButton}>
          <Image source={require('./assets/uae.png')} style={styles.flag} />
          <Text style={styles.langText}>عربي</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.langButton}>
          <Image source={require('./assets/france.png')} style={styles.flag} />
          <Text style={styles.langText}>Français</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.langButton}>
          <Image source={require('./assets/italy.png')} style={styles.flag} />
          <Text style={styles.langText}>Italiano</Text>
        </TouchableOpacity>
      </View>

      {/* زر SOS وزر اليد */}
      <View style={styles.footer}>
        <TouchableOpacity>
          <Image source={require('./assets/sos.png')} style={styles.sos} />
        </TouchableOpacity>
        <TouchableOpacity>
          <Image source={require('./assets/hand.png')} style={styles.hand} />
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', alignItems: 'center', justifyContent: 'center' },
  title: { color: '#fff', fontSize: 24, marginBottom: 20 },
  star: { width: 120, height: 120, marginBottom: 20 },
  iconRow: { flexDirection: 'row', justifyContent: 'space-between', width: '80%', marginVertical: 10 },
  icon: { width: 60, height: 60 },
  languageBar: { flexDirection: 'row', justifyContent: 'space-around', width: '100%', marginTop: 30 },
  langButton: { alignItems: 'center' },
  flag: { width: 40, height: 25 },
  langText: { color: '#fff', marginTop: 5 },
  footer: { flexDirection: 'row', justifyContent: 'space-between', width: '90%', position: 'absolute', bottom: 30 },
  sos: { width: 50, height: 50 },
  hand: { width: 50, height: 50 },
});

export default FlashDealStarHome;
