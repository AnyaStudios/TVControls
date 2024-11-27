<script>
    import { messages } from "@/stores/messages";
    import { fly } from "svelte/transition";
    import { flip } from "svelte/animate";
    import RelativeTime from "@/components/RelativeTime.svelte";
</script>

{#each $messages as { user, content, id, date } (id)}
<div 
    class="flex flex-col border shadow-sm rounded-xl bg-gray-800 border-gray-700 shadow-slate-700/[.7] mb p-4"
    in:fly={{ y: -200, duration: 500 }}
    out:fly={{ x: 500, duration: 500 }}
    animate:flip={{ duration: 500 }}
>
    
</div>
{/each}