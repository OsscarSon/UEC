import React from 'react';
import {createRoot} from 'react-dom/client';
import {Toaster, toast} from 'sonner';
import 'sonner/dist/styles.css';

const host = document.createElement('div');
host.id = 'study-notifications';
document.body.append(host);
const root = createRoot(host);

export function notify(message, type) {
  const theme = document.documentElement.dataset.theme || 'system';
  root.render(<Toaster theme={theme} position="bottom-right" richColors closeButton
    visibleToasts={3} duration={3500} mobileOffset={{ bottom: 80, left: 12, right: 12 }}
    containerAriaLabel="学习通知" />);
  const show = type === 'error' ? toast.error : type === 'success' ? toast.success : toast;
  show(message, {id: type + ':' + message});
}
