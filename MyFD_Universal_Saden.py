import streamlit as st
import { View, Text, TouchableOpacity, Image, StyleSheet } from 'react-native';

const SecureLogin = () => {
  const [message, setMessage] = useState('');

  const handleLogin = (method) => {
    let msg = '';
    switch(method) {
      case 'fingerprint':
        msg = 'مرحبًا بك! الدخول بالبصمة.';
        break;
      case 'face':
        msg = 'مرحبًا بك! الدخول بالتعرف على الوجه.';
        break;
      case 'gesture':
        msg = 'مرحبًا بك! الدخول بالإشارة.';
        break;
      case 'keypad':
        msg = 'مرحبًا بك! الدخول بالكود السري.';
        break;
      default:
        msg = '';
    }
    setMessage(msg);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>FlashDeal Star - Secure Login</Text>

      {/* الأيقونات الأربعة */}
      <View style={styles.iconRow}>
        <TouchableOpacity onPress={() => handleLogin('fingerprint')}>
          <Image source={require('./assets/images/fingerprint.png')} style={styles.icon} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => handleLogin('face')}>
          <Image source={require('./assets/images/face.png')} style={styles.icon} />
        </TouchableOpacity>
      </View>
      <View style={styles.iconRow}>
        <TouchableOpacity onPress={() => handleLogin('gesture')}>
          <Image source={require('./assets/images/gesture.png')} style={styles.icon} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => handleLogin('keypad')}>
          <Image source={require('./assets/images/keypad.png')} style={styles.icon} />
        </TouchableOpacity>
      </View>

      {/* رسالة الترحيب */}
      {message !== '' && (
        <View style={styles.messageBox}>
          <Text style={styles.message}>{message}</Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', alignItems: 'center', justifyContent: 'center' },
  title: { color: '#fff', fontSize: 22, marginBottom: 20 },
  iconRow: { flexDirection: 'row', justifyContent: 'space-around', width: '80%', marginVertical: 15 },
  icon: { width: 80, height: 80, marginHorizontal: 10 },
  messageBox: { marginTop: 30, padding: 15, backgroundColor: '#222', borderRadius: 10 },
  message: { color: '#FFD700', fontSize: 18, textAlign: 'center' },
});

export default SecureLogin;
