import {nextRevision} from './sync-contract.mjs';
import {initializeApp,getApps} from 'firebase/app';
import {getAuth,GoogleAuthProvider,signInWithPopup,signOut} from 'firebase/auth';
import {getFirestore,doc,getDoc,runTransaction,serverTimestamp} from 'firebase/firestore';
export function connect(config){const app=getApps().find(x=>x.name==='uec-study')||initializeApp(config,'uec-study'),auth=getAuth(app),db=getFirestore(app);let revision=null,owner=null;
 const ref=()=>{if(!auth.currentUser)throw Error('请先使用Google登录');if(owner!==auth.currentUser.uid){revision=null;owner=auth.currentUser.uid;}return doc(db,'users',owner,'state','current');};
 return{user:()=>auth.currentUser,async login(){await signInWithPopup(auth,new GoogleAuthProvider());revision=null;owner=null;},async logout(){await signOut(auth);revision=null;owner=null;},async read(){const snap=await getDoc(ref());if(!snap.exists()){revision=0;return null;}const value=snap.data();if(value.version!==1||!Number.isInteger(value.revision)||typeof value.payload!=='string')throw Error('云端快照格式不兼容');revision=value.revision;return{...value,updatedAt:value.updatedAt?.toDate?.().toISOString()||'服务端时间待确认'};},async upload(payload){const target=ref();const next=await runTransaction(db,async tx=>{const snap=await tx.get(target),remote=snap.exists()?snap.data().revision:0;const next=nextRevision(revision,remote);tx.set(target,{version:1,revision:next,payload,updatedAt:serverTimestamp()});return next;});revision=next;return next;}};
}
